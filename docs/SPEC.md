# SPEC: Document Summary Generator

## Overview

A web-based tool that automates the extraction and summarization of documents (PDFs, web pages) and formats Zoom meeting summaries for easy copying into Notion.

## Goals

1. **Reduce repetitive work:** Eliminate manual copy-paste workflow between documents, Claude, and Notion
2. **Save time:** Cut document processing time from 10-15 minutes to 2-3 minutes per document
3. **Consistent output:** Generate summaries in a standardized format that works well with Notion
4. **Learn skills:** Demonstrate automation capability to employer

## User Stories

### Document Summarization
- As a user, I want to upload a PDF file and receive a formatted summary so I can quickly add it to Notion
- As a user, I want to paste a URL and receive a formatted summary of that web page
- As a user, I want to see suggested AI keywords so I don't have to think of them myself
- As a user, I want to copy the formatted output with one click

### Zoom Meeting Summaries
- As a user, I want to paste a Zoom summary from email and receive it formatted for Notion
- As a user, I want to specify the meeting type so the output is properly titled

## Features (MVP - Option A)

### Core Features
1. **PDF Upload & Processing**
   - Upload PDF via drag-and-drop or file picker
   - Extract text from PDF automatically
   - Display extracted text for verification

2. **URL Processing**
   - Paste a web page URL
   - Extract main content from the page
   - Handle common article formats

3. **AI Summarization**
   - Generate general summary (comprehensive, no artificial word limit)
   - Generate section-by-section summaries (all sections, can be 40+)
   - Suggest relevant AI keywords
   - Suggest document type (Article, Report, Paper, etc.)

4. **Formatted Output**
   - Display results in Notion-ready Markdown format
   - Output structure (single page):
     1. General Summary (at the top)
     2. Section-by-Section Summaries (below, in document order)
   - One-click copy to clipboard (copies entire formatted output)
   - Clear visual separation between sections

5. **Zoom Summary Formatter**
   - Paste area for Zoom email content
   - Input field for meeting type/name
   - Format output for Notion

### Future Features (Option B - Post-MVP)
- Direct Notion API integration
- Auto-fill Notion properties (Format, URL, Type)
- Word document (.docx) support
- Automatic email monitoring for Zoom summaries

## Technology Stack

- **Backend:** Python with FastAPI
- **Frontend:** HTML, CSS, JavaScript (same approach as MICE project)
- **AI:** Claude API (Anthropic)
- **PDF Processing:** PyPDF2 or pdfplumber
- **Web Scraping:** requests + BeautifulSoup
- **Database:** None required for MVP (stateless tool)

## Acceptance Criteria

### PDF Processing
- [ ] User can upload a PDF file up to 300MB
- [ ] Text is extracted successfully (may take longer for large files)
- [ ] Handles PDFs with many pages
- [ ] Shows progress indicator for large files

### URL Processing
- [ ] User can paste any valid URL
- [ ] Tool extracts main article content (not navigation, ads, etc.)
- [ ] Handles common sites (news articles, blog posts, arXiv papers)

### Summarization
- [ ] General summary is comprehensive (length based on document complexity, no artificial limit)
- [ ] Section summaries cover ALL sections in the document (can be 40+ sections)
- [ ] Keywords are relevant to document content
- [ ] Suggested document type matches content
- [ ] For very long documents, tool processes in chunks and combines results

**Note:** Manual copy-paste to Notion supports up to ~750KB of text. For future API integration (Option B), summaries will need to be split into 2000-character blocks — this is a known workaround.

### User Interface
- [ ] Clean, simple interface with clear actions
- [ ] Copy button works and provides feedback (e.g., "Copied!")
- [ ] Error messages are helpful (e.g., "Could not extract text from PDF")
- [ ] Works in Chrome browser

### Zoom Formatter
- [ ] Accepts pasted text from Zoom email
- [ ] Outputs properly formatted Notion-ready text
- [ ] Includes meeting name/type in output

## Constraints

- Must handle large documents (up to 300MB, many pages)
- For very long documents, will use chunking strategy to process within API token limits
- Requires user to have their own Claude API key
- Output must paste cleanly into Notion without formatting issues
- Large files may take 1-2 minutes to process (progress indicator will show status)

## Out of Scope (for MVP)

- User accounts or saved history
- Notion API integration
- Word document support
- Automatic email monitoring
- Mobile-optimized interface