from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.qa import router as qa_router

app = FastAPI(
    title="AI PDF Research Assistant"
)

app.include_router(upload_router)
app.include_router(qa_router)