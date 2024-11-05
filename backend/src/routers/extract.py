# routers/extract_router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import llm

router = APIRouter(prefix='/extract', tags=["Extract"])

class TextData(BaseModel):
    extracted_text: str

@router.post("/")
async def extract_information(text_data: TextData):
    extracted_info = await llm.extract_entities(text_data.extracted_text)
    if not extracted_info:
        raise HTTPException(status_code=500, detail="Failed to extract information from text")
    return extracted_info
