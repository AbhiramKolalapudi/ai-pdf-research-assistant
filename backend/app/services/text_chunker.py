from app.models.document_chunk import DocumentChunk
from app.models.document_page import DocumentPage


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
        pages: list[DocumentPage],
        document: str
    ):

        chunks = []
        chunk_id = 0

        for page in pages:

            page_chunks, chunk_id = self._chunk_page(
                page,
                document,
                chunk_id
            )

            chunks.extend(page_chunks)

        return chunks

    def _chunk_page(
        self,
        page: DocumentPage,
        document: str,
        chunk_id: int
    ):

        chunks = []

        paragraphs = page.text.split("\n\n")

        current_chunk = ""

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            # Huge paragraph
            if len(paragraph) > self.chunk_size:

                if current_chunk:

                    chunks.append(
                        DocumentChunk(
                            document=document,
                            page=page.number,
                            chunk_id=chunk_id,
                            text=current_chunk
                        )
                    )

                    chunk_id += 1
                    current_chunk = ""

                large_chunks, chunk_id = self._split_large_paragraph(
                    paragraph,
                    page,
                    document,
                    chunk_id
                )

                chunks.extend(large_chunks)

                continue

            # Paragraph fits
            if len(current_chunk) + len(paragraph) <= self.chunk_size:

                if current_chunk:
                    current_chunk += "\n\n"

                current_chunk += paragraph

            else:

                chunks.append(
                    DocumentChunk(
                        document=document,
                        page=page.number,
                        chunk_id=chunk_id,
                        text=current_chunk
                    )
                )

                chunk_id += 1

                current_chunk = paragraph

        if current_chunk:

            chunks.append(
                DocumentChunk(
                    document=document,
                    page=page.number,
                    chunk_id=chunk_id,
                    text=current_chunk
                )

            )

            chunk_id += 1

        return chunks, chunk_id

    def _split_large_paragraph(
        self,
        paragraph,
        page,
        document,
        chunk_id
    ):

        chunks = []

        start = 0

        while start < len(paragraph):

            end = start + self.chunk_size

            chunks.append(

                DocumentChunk(
                    document=document,
                    page=page.number,
                    chunk_id=chunk_id,
                    text=paragraph[start:end]
                )

            )

            chunk_id += 1

            start = end - self.overlap

        return chunks, chunk_id