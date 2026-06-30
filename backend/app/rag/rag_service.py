from app.services.vector_store import VectorStore
from app.services.prompt_builder import PromptBuilder
from app.services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.vector_store = VectorStore()

        self.prompt_builder = PromptBuilder()

        self.llm_service = LLMService()

    def answer(
        self,
        question: str
    ) -> str:

        results = self.vector_store.search(
            question
        )

        prompt = self.prompt_builder.build(
            results,
            question
        )

        return self.llm_service.generate(
            prompt
        )
