import fitz


class PDFParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = []

        with fitz.open(self.pdf_path) as document:
            for page in document:
                page_text = page.get_text("text")
                text.append(page_text)

        return "".join(text)