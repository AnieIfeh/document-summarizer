# BRAINSTORM: Document Summary Generator

## What problem am I solving?

I spend significant time each week processing documents for my team's Notion knowledge base. The current workflow is tedious and repetitive:

1. Receive document assignment via Linear
2. Open the document (could be PDF, Word doc, or web link)
3. Manually copy content into Claude
4. Prompt Claude for a general summary and section-by-section summaries
5. Copy Claude's output back into Notion
6. Manually fill in properties (Type, Format, URL, AI keywords, etc.)

For 5-10 documents per week, this adds up to hours of repetitive copy-paste work. The summarization step is the biggest time sink.

## What would the ideal solution look like?

A tool where I can:
- Drop in a file (PDF, Word) or paste a URL
- Click one button
- Get back a nicely formatted output with:
  - General summary
  - Section-by-section summaries
  - Suggested AI keywords
  - Document metadata (title, date published if detectable)
- Copy the formatted output directly into Notion

Future enhancement: The tool could connect directly to Notion and create the page for me with properties pre-filled.

## What's the minimum viable version (MVP)?

A Python script or simple web interface that:
- Accepts a PDF file OR a URL
- Extracts the text content
- Sends it to an AI API for summarization
- Returns formatted summaries ready to paste into Notion

Word docs can be added later. Start with PDFs and URLs since those are most common.

## What technologies/tools might I use?

**Definitely using:**
- Python (familiar from MICE project)
- Claude API or OpenAI API for summarization

**For text extraction:**
- PyPDF2 or pdfplumber for PDFs
- requests + BeautifulSoup for web pages
- python-docx for Word docs (future)

**For the interface:**
- Option 1: Command line tool (simplest)
- Option 2: Simple web interface with FastAPI (familiar from MICE project)
- Option 3: Streamlit (easy UI, less code)

**Future (Option B):**
- Notion API for direct integration

## Decisions Made

1. **Interface:** Web interface with buttons (familiar from MICE project, easier to use daily)
2. **AI API:** Claude API (same quality I'm used to from manual workflow)
3. **Output format:** Markdown (pastes cleanly into Notion, readable human language)

## Open questions (to resolve in SPEC)

1. How should I handle very long documents that exceed token limits?
2. How specific should the section-by-section summaries be?

## Constraints

- Must work with PDFs and web URLs at minimum
- Should output in a format that pastes cleanly into Notion
- Need to handle API costs (my own API key)
- Should be simple enough to complete in a reasonable timeframe

## Zoom Meeting Summaries

In addition to documents, I also need to add Zoom meeting summaries to Notion:

- Boss forwards Zoom summaries via email (in the email body, not attachments)
- Zoom already provides the summary text, so no AI summarization needed
- I need to name the Notion entry based on meeting type
- Currently this is manual copy-paste from email to Notion

**For MVP:** Manual trigger — paste in the email content, tool formats it for Notion
**Future enhancement:** Automatic email monitoring (only if time permits, not critical for MVP)

## Notes / Raw thoughts

- Keywords suggestion would be really helpful since I have to think of those manually
- Would be nice if it detected the document type (Article, Report, etc.) automatically
- Maybe include a "copy to clipboard" button if it has a UI
- Zoom summaries are simpler since no AI processing needed, just formatting