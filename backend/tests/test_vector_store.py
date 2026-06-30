from app.rag.ingestion_pipeline import IngestionPipeline
from app.services.vector_store import VectorStore

PDF_PATH = "data/uploads/AI.pdf"


pipeline = IngestionPipeline()

chunks = pipeline.process(PDF_PATH)

print(f"Generated {len(chunks)} chunks")


vector_store = VectorStore()

vector_store.add_chunks(chunks)

print("Chunks stored successfully!")


results = vector_store.search(
    "What is machine learning?"
)

print()

print("Search Results")

print("-" * 50)

for result in results:

    print(f"Distance : {result.distance:.4f}")
    print(f"Document : {result.chunk.document}")
    print(f"Page     : {result.chunk.page}")
    print(f"Chunk ID : {result.chunk.chunk_id}")
    print()
    print(result.chunk.text)
    print("=" * 60)