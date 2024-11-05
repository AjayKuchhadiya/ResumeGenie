from fastapi import APIRouter, UploadFile, File, HTTPException
from services import ocr, llm  # Import the LLM service

router = APIRouter(prefix='/upload', tags=["Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Process the file and extract text
    extracted_text = await ocr.extract_text(file)

    # Extract structured information using LLM
    structured_data = llm.extract_entities(extracted_text)

    return structured_data