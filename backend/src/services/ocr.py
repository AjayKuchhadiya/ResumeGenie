# services/ocr_service.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from io import BytesIO
from docx import Document
from fastapi import UploadFile

async def extract_text(file: UploadFile) -> str:
    """
    Extracts text from a PDF or DOCX file. Uses OCR if the PDF contains images.
    """
    # Check file type and call appropriate extraction function
    if file.content_type == "application/pdf":
        return await _extract_text_from_pdf(file)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return _extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file type")

async def _extract_text_from_pdf(file: UploadFile) -> str:
    """
    Extracts text from a PDF file. Uses OCR if the PDF contains images.
    """
    pdf_data = await file.read()
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
    text = ""

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text()

        # If page has no text, assume it's an image and use OCR
        if not page_text.strip():
            pix = page.get_pixmap()
            img = Image.open(BytesIO(pix.tobytes("png")))
            page_text = pytesseract.image_to_string(img)

        text += page_text + "\n"
    
    pdf_document.close()
    return text.strip()

def _extract_text_from_docx(file: UploadFile) -> str:
    """
    Extracts text from a DOCX file.
    """
    docx_data = BytesIO(file.file.read())
    document = Document(docx_data)
    text = "\n".join([para.text for para in document.paragraphs])
    return text.strip()
