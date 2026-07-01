from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.api.dependencies import get_knowledge_base
from app.api.schemas import UploadResponse
from app.services.knowledge_base_service import KnowledgeBaseService
from app.settings import settings

router = APIRouter(tags=["Upload"])


@router.post(
    "/upload",
    response_model=UploadResponse,
)
async def upload_pdf(
    file: UploadFile = File(...),
    knowledge_base: KnowledgeBaseService = Depends(get_knowledge_base),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = upload_dir / file.filename

    with pdf_path.open("wb") as buffer:
        buffer.write(await file.read())

    knowledge_base.ingest(str(pdf_path))

    return UploadResponse(
        message="PDF indexed successfully."
    )