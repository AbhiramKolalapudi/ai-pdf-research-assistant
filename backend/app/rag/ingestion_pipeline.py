from pathlib import Path

from app.services.pdf_parser import PDFParser
from app.services.text_cleaner import TextCleaner
from app.services.text_chunker import TextChunker


class IngestionPipeline:

    def __init__(self):
        self.cleaner = TextCleaner()
        self.chunker = TextChunker()

    def process(self, pdf_path):

        parser = PDFParser(pdf_path)

        pages = parser.extract_text()

        for page in pages:
            page.text = self.cleaner.clean(page.text)

        document_name = Path(pdf_path).name

        chunks = self.chunker.chunk(
            pages,
            document=document_name
        )

        return chunks