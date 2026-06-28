# AI-Powered PDF Research Assistant

## Day 1 - Project Foundation & Backend Setup

**Date:** 27 June 2026

### Objectives
- Set up the development environment.
- Initialize Git and GitHub.
- Build the first FastAPI backend.

### Work Completed
- Installed and configured Git.
- Created the GitHub repository.
- Designed the project folder structure.
- Created a Python virtual environment.
- Installed FastAPI and Uvicorn.
- Built and ran the first FastAPI application.
- Verified the API using Swagger UI.

### Concepts Learned
- RAG overview
- Embeddings
- Semantic search
- Vector databases
- Document chunking
- Git workflow
- Virtual environments
- FastAPI & Uvicorn
- HTTP (GET & POST)
- Swagger UI

### Files Added
- `backend/app/main.py`
- `.gitignore`
- `README.md`
- `backend/requirements.txt`
- `backend/.env.example`

### Git Commit
```
Setup project structure and FastAPI backend
```

### Next Session
- PDF parsing
- Text extraction using PyMuPDF
- Text cleaning
- Document chunking

## Day 2 - Document Processing Pipeline

**Date:** 28 June 2026

### Objectives
- Parse PDF documents.
- Extract readable text.
- Clean extracted text.
- Split documents into chunks.
- Design metadata models.

### Work Completed
- Learned how PDFs store information.
- Built a PDF parser using PyMuPDF.
- Built a text cleaning service.
- Implemented an overlapping text chunker.
- Designed a `DocumentChunk` model using dataclasses.
- Built the ingestion pipeline architecture.

### Concepts Learned
- PDF internals
- Document & Page objects
- Raw text extraction
- Text preprocessing
- Single Responsibility Principle
- Overlapping chunking
- Metadata
- Dataclasses
- Object composition
- Ingestion pipelines

### Files Added
- `backend/app/services/pdf_parser.py`
- `backend/app/services/text_cleaner.py`
- `backend/app/services/text_chunker.py`
- `backend/app/models/document_chunk.py`
- `backend/app/rag/ingestion_pipeline.py`

### Git Commit
```
Implement PDF ingestion pipeline with parsing, cleaning, chunking and metadata
```

### Next Session
- Improve chunking strategy
- Generate embeddings
- Store embeddings in ChromaDB
- Semantic similarity search