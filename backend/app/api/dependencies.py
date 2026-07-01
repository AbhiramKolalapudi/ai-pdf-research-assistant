from app.rag.rag_service import RAGService
from app.services.knowledge_base_service import KnowledgeBaseService


def get_knowledge_base() -> KnowledgeBaseService:
    return KnowledgeBaseService()


def get_rag_service() -> RAGService:
    return RAGService()