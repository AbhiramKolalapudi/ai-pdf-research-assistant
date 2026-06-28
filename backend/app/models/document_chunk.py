from dataclasses import dataclass

@dataclass
class DocumentChunk:
    document: str
    chunk_id: int
    text: str