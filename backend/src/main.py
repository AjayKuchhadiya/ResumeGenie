# main.py
from fastapi import FastAPI
from routers import upload, extract
import uvicorn

app = FastAPI()

# Include the routers
app.include_router(upload.router)
app.include_router(extract.router)

# Root endpoint (optional)
@app.get("/")
async def root():
    return {"message": "Resume Extractor API is running"}


if __name__ == '__main__':
    uvicorn.run("main:app", host= 'localhost', port=8000, reload=True)