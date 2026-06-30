from sentence_transformers import SentenceTransformer
from app.settings import settings


class EmbeddingService:

    def __init__(
        self
    ):
        self.model = SentenceTransformer(settings.embedding_model)

    def embed(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()