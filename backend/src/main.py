from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only the frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the routers
app.include_router(upload.router)

# Root endpoint (optional)
@app.get("/")
async def root():
    return {"message": "Resume Extractor API is running"}


if __name__ == '__main__':
    uvicorn.run("main:app", host= 'localhost', port=8000, reload=True)