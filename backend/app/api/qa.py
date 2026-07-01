from fastapi import APIRouter, Depends

from app.api.dependencies import get_rag_service
from app.api.schemas import AskRequest, AskResponse
from app.rag.rag_service import RAGService

router = APIRouter(tags=["Question Answering"])


@router.post(
    "/ask",
    response_model=AskResponse,
)
async def ask_question(
    request: AskRequest,
    rag_service: RAGService = Depends(get_rag_service),
):
    answer = rag_service.answer(
        request.question
    )

    return AskResponse(
        answer=answer
    )