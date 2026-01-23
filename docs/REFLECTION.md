# Project Reflection: Document Summary Generator

**Author:** Ifeh  
**Date:** January 23, 2026  
**Course:** Elite AI Assisted Coding - Cohort 2

---

## What I Built

I built a Document Summary Generator that helps me with my operational duty of adding documents to Notion. The tool can:

- Extract text from PDF files
- Extract content from web pages
- Format Zoom meeting summaries
- Generate AI-powered summaries using Claude
- Output everything in a Notion-ready format with one-click copy

---

## What Worked Well

1. **The Spec Flow Process** - Starting with BRAINSTORM.md, then SPEC.md, then TASKS.md helped me organize my thoughts before writing code. Breaking the project into phases made it less overwhelming.

2. **Building on Previous Knowledge** - Using the same Python/FastAPI stack from my MICE Quotient project meant I wasn't starting from scratch. I understood concepts like endpoints, HTML templates, and JavaScript interactions.

3. **Step-by-Step Guidance** - Working through each phase one step at a time helped me understand what each piece of code does, rather than just copying without learning.

4. **The Claude API Integration** - Connecting to Claude's API was simpler than I expected. The hardest part was setting up the API key securely with the .env file.

---

## What Was Challenging

1. **Understanding API Errors** - When I first got the "credit balance too low" error, I wasn't sure if it was a code problem or an account problem. Learning to read error messages carefully is an important skill.

2. **Keeping Track of Files** - With multiple folders (backend, frontend, docs) and multiple files, it sometimes took a moment to find the right file to edit.

3. **Waiting for API Responses** - The summarization takes 15-30 seconds, which felt long at first. I learned this is normal for AI API calls processing large amounts of text.

---

## What I Learned

1. **How to integrate external APIs** - I now understand how to send requests to an API and handle the responses.

2. **Environment variables for secrets** - Using a .env file to store API keys keeps them secure and out of the code.

3. **Web scraping basics** - Using requests and BeautifulSoup to extract content from web pages.

4. **Building a complete tool** - From idea to working application, I experienced the full development process.

---

## How This Helps My Work

This tool directly solves a real problem I have at work. Instead of manually reading documents and writing summaries for Notion, I can now:

1. Upload a PDF or paste a URL
2. Get an AI-generated summary in seconds
3. Copy and paste directly into Notion

This will save me significant time on my operational duties.

---

## Next Steps (Future Improvements)

If I continue developing this tool, I would add:

- Direct Notion API integration (auto-post summaries)
- Support for Word documents (.docx)
- Batch processing (multiple files at once)
- History of previous summaries

---

## Conclusion

This project showed me that with AI assistance, I can build practical tools that solve real problems in my daily work. The combination of clear planning (Spec Flow) and step-by-step implementation made a project that once seemed complex feel achievable.