from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

embedding = service.embed("Machine learning is amazing.")

print(len(embedding))
print(embedding[:5])