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

## Day 4 - Retrieval-Augmented Generation (RAG) & LLM Integration

**Date:** 30 June 2026

### Objectives
- Review and improve the backend architecture.
- Introduce centralized application configuration.
- Connect semantic retrieval with a Large Language Model.
- Build the Retrieval-Augmented Generation (RAG) pipeline.
- Generate grounded answers using retrieved document context.

### Work Completed
- Introduced centralized configuration using `pydantic-settings`.
- Learned the purpose of `.env` and `.env.example`.
- Built a `Settings` object for application configuration.
- Refactored `EmbeddingService` to use centralized settings.
- Refactored `VectorStore` to use configurable settings and retrieval parameters.
- Designed and implemented a `Prompt` model.
- Built a `PromptBuilder` service for prompt engineering.
- Integrated Google's Gemini API using the new `google-genai` SDK.
- Built an `LLMService`.
- Built a `RAGService` to orchestrate retrieval, prompt construction and answer generation.
- Built a `KnowledgeBaseService` to encapsulate document ingestion and indexing.
- Successfully generated answers from uploaded PDFs using Retrieval-Augmented Generation.
- Reviewed and refined the backend architecture by separating ingestion and retrieval workflows.

### Concepts Learned
- Large Language Models (LLMs)
- Prompt Engineering
- System Prompt vs User Prompt
- Retrieval-Augmented Generation (RAG)
- Google Gemini API
- Environment variables
- `.env` and `.env.example`
- Centralized configuration
- `pydantic-settings`
- Value Objects
- Orchestrator pattern
- Integration testing
- Separation of ingestion and retrieval workflows
- Backend architecture and service orchestration

### Files Added
- `backend/app/settings.py`
- `backend/app/models/prompt.py`
- `backend/app/services/prompt_builder.py`
- `backend/app/services/llm_service.py`
- `backend/app/services/knowledge_base_service.py`
- `backend/app/rag/rag_service.py`
- `backend/tests/test_rag.py`

### Files Modified
- `backend/app/services/embedding_service.py`
- `backend/app/services/vector_store.py`
- `backend/.env.example`
- `backend/requirements.txt`

### Git Commit
```
Implement Retrieval-Augmented Generation with Gemini LLM integration
```

### Next Session
- Build FastAPI upload endpoint.
- Build question-answer endpoint.
- Connect backend services with FastAPI.
- Test the API using Swagger UI.
- Review and polish the overall project architecture.