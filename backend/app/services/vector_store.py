import chromadb

from app.models.document_chunk import DocumentChunk
from app.models.search_result import SearchResult
from app.services.embedding_service import EmbeddingService


class VectorStore:

    def __init__(
        self,
        db_path: str = "./chroma_db"
    ):

        self.client = chromadb.PersistentClient(
            path=db_path
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.embedding_service = EmbeddingService()

    def add_chunks(
        self,
        chunks: list[DocumentChunk]
    ):

        ids = []
        documents = []
        metadatas = []
        embeddings = []

        for chunk in chunks:

            ids.append(
                f"{chunk.document}_{chunk.chunk_id}"
            )

            documents.append(
                chunk.text
            )

            metadatas.append(
                {
                    "document": chunk.document,
                    "page": chunk.page,
                    "chunk_id": chunk.chunk_id
                }
            )

            embeddings.append(
                self.embedding_service.embed(
                    chunk.text
                )
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ) -> list[SearchResult]:

        query_embedding = self.embedding_service.embed(
            query
        )

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        search_results = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            chunk = DocumentChunk(
                document=metadata["document"],
                page=metadata["page"],
                chunk_id=metadata["chunk_id"],
                text=document
            )

            search_results.append(
                SearchResult(
                    chunk=chunk,
                    distance=distance
                )
            )

        return search_results