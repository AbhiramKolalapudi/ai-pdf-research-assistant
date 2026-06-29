from dataclasses import dataclass

from app.models.document_chunk import DocumentChunk


@dataclass
class SearchResult:
    chunk: DocumentChunk
    distance: float