from dataclasses import dataclass

@dataclass
class DocumentChunk:
    document: str
    page: int
    chunk_id: int
    text: str