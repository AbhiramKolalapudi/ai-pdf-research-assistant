from app.rag.ingestion_pipeline import IngestionPipeline
from app.rag.rag_service import RAGService

PDF_PATH = "data/uploads/AI.pdf"


print("Processing PDF...")

pipeline = IngestionPipeline()

chunks = pipeline.process(PDF_PATH)

print(f"Generated {len(chunks)} chunks")


rag = RAGService()

print("Indexing document...")

rag.vector_store.add_chunks(chunks)

print("Document indexed successfully!")


print()

question = "What is machine learning?"

print(f"Question: {question}")

print("-" * 60)

answer = rag.answer(question)

print(answer)