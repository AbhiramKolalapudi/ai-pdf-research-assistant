from app.rag.ingestion_pipeline import IngestionPipeline
from app.services.vector_store import VectorStore


class KnowledgeBaseService:

    def __init__(self):

        self.pipeline = IngestionPipeline()

        self.vector_store = VectorStore()

    def ingest(
        self,
        pdf_path: str
    ) -> None:

        chunks = self.pipeline.process(
            pdf_path
        )

        self.vector_store.add_chunks(
            chunks
        )