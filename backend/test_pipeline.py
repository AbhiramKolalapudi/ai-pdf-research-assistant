from app.rag.ingestion_pipeline import IngestionPipeline

pipeline = IngestionPipeline()

chunks = pipeline.process(
    "data/uploads/AI.pdf"
)

for chunk in chunks:
    print(chunk)
    print("-" * 50)