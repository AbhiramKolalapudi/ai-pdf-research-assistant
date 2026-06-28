from app.models.document_chunk import DocumentChunk


class TextChunker:

    def __init__(
        self,
        chunk_size=1000,
        overlap=200
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(
        self,
        text: str,
        document: str
    ):

        chunks = []

        start = 0
        chunk_id = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(
                DocumentChunk(
                    document=document,
                    chunk_id=chunk_id,
                    text=text[start:end]
                )
            )

            chunk_id += 1

            start = end - self.overlap

        return chunks