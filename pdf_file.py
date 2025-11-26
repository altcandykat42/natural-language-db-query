from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import os
import fitz
STORE_DIR = "store"

router = APIRouter(prefix="/pdf", tags=["pdf"])
# # doc = fitz.open("test.pdf")
# doc = fitz.open("fail_test.pdf")
# toc = doc.get_toc()
# print(toc)

@router.post("/upload")
async def upload_pdf(
    pdf_file: UploadFile = File(...),
    file_name: str = Form(...)
):
    # Validate file type
    if pdf_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    # Create full path with custom name
    file_path = os.path.join(STORE_DIR, f"{file_name}.pdf")

    # Check if file already exists
    if os.path.exists(file_path):
        raise HTTPException(status_code=409, detail="File name already exists.")

    # Save file to disk
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(await pdf_file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to save file.")

    return JSONResponse(content={"message": "File uploaded successfully."}, status_code=200)


@router.get("/all")
async def list_pdfs():
    try:
        files = os.listdir(STORE_DIR)
        return JSONResponse(content={"files": files}, status_code=200)
    except Exception as e:
        raise HTTPException(e)
    
@router.delete("/delete/{filename}")
def delete_pdf(filename: str):
    file_path = os.path.join(STORE_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        os.remove(file_path)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to delete file")

    return JSONResponse(content={"message": "File deleted"}, status_code=200)