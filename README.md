# Document Summary Generator

A web-based tool that extracts text from PDFs and web pages, then uses AI to generate structured summaries ready for Notion.

Built as part of the Elite AI Assisted Coding course (HW2).

---

## Features

### 1. PDF Upload
- Upload any PDF document
- Automatically extracts text from all pages
- Generates AI-powered summary

### 2. URL Extract
- Paste any web page URL
- Extracts main article content (ignores ads, navigation, etc.)
- Generates AI-powered summary

### 3. Zoom Summary Formatter
- Paste Zoom meeting summaries from email
- Add meeting name and type
- Formats output for easy pasting into Notion

### All Summaries Include:
- **General Summary** - Overview of the entire document
- **Section-by-Section Summary** - Breakdown of main topics
- **Keywords** - Key terms and concepts
- **Document Type** - Classification (Article, Report, etc.)
- **One-click copy** - Copy formatted text to clipboard

---

## Technology Stack

- **Backend:** Python with FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **AI:** Claude API (Anthropic)
- **PDF Processing:** pdfplumber
- **Web Scraping:** requests + BeautifulSoup

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Anthropic API key (get one at https://console.anthropic.com)

### Installation

1. **Clone or download this project**

2. **Open the project folder in your terminal**

3. **Create a virtual environment:**
```
   python -m venv venv
```

4. **Activate the virtual environment:**
   
   On Windows:
```
   venv\Scripts\activate
```
   
   On Mac/Linux:
```
   source venv/bin/activate
```

5. **Install dependencies:**
```
   pip install fastapi uvicorn python-multipart pdfplumber requests beautifulsoup4 anthropic python-dotenv
```

6. **Create a .env file** in the project root with your API key:
```
   ANTHROPIC_API_KEY=your-api-key-here
```

7. **Start the server:**
```
   uvicorn backend.main:app --reload
```

8. **Open your browser** and go to:
```
   http://127.0.0.1:8000
```

---

## How to Use

### PDF Upload
1. Click the "PDF Upload" tab
2. Drag and drop a PDF file, or click to select one
3. Click "Extract & Summarize"
4. Wait for the AI to generate a summary
5. Click "Copy to Clipboard" to copy the result

### URL Extract
1. Click the "URL Extract" tab
2. Paste a web page URL in the input field
3. Click "Extract & Summarize"
4. Wait for the AI to generate a summary
5. Click "Copy to Clipboard" to copy the result

### Zoom Summary
1. Click the "Zoom Summary" tab
2. Enter the meeting name and type
3. Paste the Zoom meeting summary from your email
4. Click "Format for Notion"
5. Click "Copy to Clipboard" to copy the result

---

## Project Structure
```
document-summarizer/
├── backend/
│   └── main.py          # FastAPI server and API endpoints
├── frontend/
│   └── index.html       # User interface
├── docs/
│   ├── BRAINSTORM.md    # Initial ideas
│   ├── SPEC.md          # Project specification
│   └── TASKS.md         # Task breakdown
├── .env                 # API key (not shared)
└── README.md            # This file
```

---

## Author

Built by Ifeh as part of the Elite AI Assisted Coding course, January 2026.