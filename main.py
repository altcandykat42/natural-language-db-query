from fastapi import FastAPI
from pdf_file import router as pdf_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fast Summarizer API!"}