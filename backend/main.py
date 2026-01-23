from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pdfplumber
import requests
from bs4 import BeautifulSoup
import anthropic
import os
import io
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the FastAPI app
app = FastAPI(title="Document Summary Generator")

# Get the path to the frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

# Serve static files (CSS, JavaScript) from the frontend folder
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class URLRequest(BaseModel):
    """Model for URL input"""
    url: str


class SummarizeRequest(BaseModel):
    """Model for summarization input"""
    text: str
    source_type: str = "document"


class ZoomRequest(BaseModel):
    """Model for Zoom summary input"""
    meeting_name: str
    meeting_type: str
    zoom_summary: str


@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    return FileResponse(os.path.join(frontend_path, "index.html"))


@app.get("/health")
async def health_check():
    """Simple endpoint to verify the server is running"""
    return {"status": "healthy", "message": "Document Summary Generator is running!"}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and extract its text content.
    Returns the extracted text.
    """
    if not file.filename.lower().endswith('.pdf'):
        return {"error": "File must be a PDF"}
    
    try:
        contents = await file.read()
        pdf_file = io.BytesIO(contents)
        
        extracted_text = ""
        with pdfplumber.open(pdf_file) as pdf:
            total_pages = len(pdf.pages)
            for page_num, page in enumerate(pdf.pages, 1):
                page_text = page.extract_text()
                if page_text:
                    extracted_text += f"\n--- Page {page_num} ---\n"
                    extracted_text += page_text
        
        return {
            "success": True,
            "filename": file.filename,
            "total_pages": total_pages,
            "extracted_text": extracted_text,
            "text_length": len(extracted_text)
        }
    
    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}


@app.post("/extract-url")
async def extract_url(request: URLRequest):
    """
    Fetch a web page URL and extract its main text content.
    Returns the extracted text.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(request.url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            element.decompose()
        
        main_content = None
        
        for selector in ['article', 'main', '[role="main"]', '.article', '.post', '.content']:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        if not main_content:
            main_content = soup.body
        
        if main_content:
            text_elements = main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
            extracted_text = ""
            
            for element in text_elements:
                text = element.get_text(strip=True)
                if text:
                    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                        extracted_text += f"\n\n## {text}\n"
                    else:
                        extracted_text += f"{text}\n\n"
        else:
            extracted_text = soup.get_text(separator='\n', strip=True)
        
        title = soup.title.string if soup.title else "No title found"
        
        return {
            "success": True,
            "url": request.url,
            "title": title,
            "extracted_text": extracted_text,
            "text_length": len(extracted_text)
        }
    
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. The website took too long to respond."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch URL: {str(e)}"}
    except Exception as e:
        return {"error": f"Failed to process URL: {str(e)}"}


@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    """
    Send text to Claude API and get a structured summary.
    Returns general summary, section summaries, keywords, and document type.
    """
    try:
        prompt = f"""You are a document summarization assistant. Analyze the following text and provide a comprehensive, detailed summary.

Please provide your response in the following format:

## General Summary
Can you please provide me with a detailed structured summary of this report, including any appendices. Be extremely thorough and capture ALL key points, findings, recommendations, and conclusions. Do not leave out important details. The summary should be comprehensive enough that someone could understand the full scope of the document without reading it.

## Section-by-Section Summary
Can you please provide me with a detailed structured summary of each section of this report, including any appendices. For EVERY section, subsection, and appendix in the document:
- Clearly label each section with its original heading
- Provide a thorough summary of that section's content
- Include specific details, data points, and findings mentioned
- Do not skip any sections, even if they seem minor

## AI Keywords
[List 5-10 relevant keywords or key phrases that describe the main topics, separated by commas]

## Document Type
[Identify the type of document: Article, Research Paper, Report, Blog Post, News Article, Tutorial, Documentation, or Other]

Here is the text to summarize:

{request.text}
"""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8096,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        summary_response = message.content[0].text
        
        return {
            "success": True,
            "source_type": request.source_type,
            "summary": summary_response,
            "input_length": len(request.text),
            "output_length": len(summary_response)
        }
    
    except anthropic.APIError as e:
        return {"error": f"Claude API error: {str(e)}"}
    except Exception as e:
        return {"error": f"Failed to summarize: {str(e)}"}


@app.post("/format-zoom")
async def format_zoom(request: ZoomRequest):
    """
    Format a Zoom meeting summary for Notion.
    Returns formatted text ready to paste into Notion.
    """
    try:
        formatted_output = f"""# {request.meeting_name}

**Meeting Type:** {request.meeting_type}

---

## Meeting Summary

{request.zoom_summary}

---

*Formatted for Notion by Document Summary Generator*
"""
        
        return {
            "success": True,
            "meeting_name": request.meeting_name,
            "meeting_type": request.meeting_type,
            "formatted_output": formatted_output,
            "output_length": len(formatted_output)
        }
    
    except Exception as e:
        return {"error": f"Failed to format Zoom summary: {str(e)}"}