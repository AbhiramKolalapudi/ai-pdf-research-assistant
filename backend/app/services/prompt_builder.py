from app.models.search_result import SearchResult
from app.models.prompt import Prompt


class PromptBuilder:

    SYSTEM_PROMPT = """
You are a helpful PDF research assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, clearly state that the information is not available in the provided documents.

Do not make up facts or use outside knowledge.

Provide clear and concise answers.
"""

    def build(
        self,
        results: list[SearchResult],
        question: str
    ) -> Prompt:

        parts = []

        for result in results:

            parts.append(
            f"Document: {result.chunk.document}\n"
            f"Page: {result.chunk.page}\n\n"
            f"{result.chunk.text}\n\n"
            + "-" * 50
            + "\n\n"
        )

        context = "".join(parts)

        user_prompt = f"""
Use the following context to answer the user's question.

Context:

{context}

Question:
{question}
"""

        return Prompt(system=self.SYSTEM_PROMPT,user=user_prompt)