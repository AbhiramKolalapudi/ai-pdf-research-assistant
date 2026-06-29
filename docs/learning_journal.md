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

## Day 3 - Embeddings, Vector Database & Semantic Search

**Date:** 29 June 2026

### Objectives
- Preserve page metadata throughout the ingestion pipeline.
- Improve document chunking.
- Learn embeddings conceptually.
- Generate embeddings.
- Store embeddings in a vector database.
- Implement semantic similarity search.

### Work Completed
- Refactored the PDF parser to preserve page information.
- Introduced the `DocumentPage` model.
- Updated the ingestion pipeline to process pages individually.
- Implemented paragraph-aware chunking with character-overlap fallback.
- Added page metadata to `DocumentChunk`.
- Built an `EmbeddingService` using Sentence Transformers.
- Generated 384-dimensional embeddings using `all-MiniLM-L6-v2`.
- Learned cosine similarity and semantic retrieval.
- Integrated ChromaDB as the vector database.
- Built a `VectorStore` service.
- Implemented batch insertion of document chunks.
- Implemented semantic search returning `SearchResult` objects.
- Successfully indexed and queried a PDF using semantic search.

### Concepts Learned
- Page-aware document processing
- Hierarchical chunking
- Paragraph-aware chunking
- Embeddings
- Sentence Transformers
- Vector representations
- Cosine similarity
- Nearest-neighbor search
- Vector databases
- ChromaDB
- Batch insertion
- Semantic search
- Service abstraction
- Separation of responsibilities

### Files Added
- `backend/app/models/document_page.py`
- `backend/app/models/search_result.py`
- `backend/app/services/embedding_service.py`
- `backend/app/services/vector_store.py`
- `backend/tests/test_embedding.py`
- `backend/tests/test_vector_store.py`

### Files Modified
- `backend/app/models/document_chunk.py`
- `backend/app/services/pdf_parser.py`
- `backend/app/services/text_chunker.py`
- `backend/app/rag/ingestion_pipeline.py`
- `backend/requirements.txt`

### Git Commit
```text
Implement semantic search with embeddings and ChromaDB
```

### Next Session
- Review and polish the current architecture.
- Improve project structure and configuration.
- Connect retrieval with an LLM.
- Build the Retrieval-Augmented Generation (RAG) pipeline.
- Generate answers using retrieved context.
- Expose the functionality through FastAPI endpoints.