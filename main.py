from fastapi import FastAPI, File, UploadFile, HTTPException, status
from src.upload import *
import shutil

app = FastAPI()

@app.post("/upload/{user_id}/{report_id}/")
async def upload_and_process_mp4(user_id: str, report_id: str, file: UploadFile = File(...)):
    if file.content_type != "video/mp4":
        raise HTTPException(status_code=400, detail="Invalid file type")
    tmp_file_path = f"temp/{file.filename}"
    with open(tmp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    output_dir = f"frames/{user_id}/{report_id}/"
    saveFrames(tmp_file_path, output_dir)
    os.remove(tmp_file_path)
    return {"message": "Done"}

@app.get('/users/{user_id}/{report_id}/', status_code=status.HTTP_200_OK)
async def get_report(user_id: str, report_id: str):
    return {"message": "Done"}

@app.delete('/users/{user_id}/{report_id}/', status_code=status.HTTP_200_OK)
async def delete_report(user_id: str, report_id: str):
    return {"message": "Done"}