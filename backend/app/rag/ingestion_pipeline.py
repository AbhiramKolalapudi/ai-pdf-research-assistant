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

        raw_text = parser.extract_text()

        clean_text = self.cleaner.clean(raw_text)

        document_name = Path(pdf_path).name

        chunks = self.chunker.chunk(
            clean_text,
            document=document_name
        )

        return chunks