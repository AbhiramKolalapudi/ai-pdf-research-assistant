import fitz

from app.models.document_page import DocumentPage


class PDFParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_text(self) -> list[DocumentPage]:
        pages = []

        with fitz.open(self.pdf_path) as document:
            for page in document:
                page_text = page.get_text("text")

                pages.append(
                    DocumentPage(
                        number=page.number + 1,  # Convert 0-based index to 1-based
                        text=page_text
                    )
                )

        return pages