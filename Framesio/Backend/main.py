from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.staticfiles import StaticFiles
from .src.upload import saveFrames
import shutil
import os
from .src.rand import get_random_string_number
from fastapi.middleware.cors import CORSMiddleware

fapp = FastAPI()

# @fapp.get("/api/hello")
async def gethello():
    return {"hello": "heelo"}

@fapp.post("/upload")
async def upload_and_process_mp4(file: UploadFile = File(...)):
    if file.content_type != "video/mp4":
        raise HTTPException(status_code=400, detail="Invalid file type")
    tmp_file_path = f"temp/{file.filename}"
    with open(tmp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    folder_name = get_random_string_number(20)
    output_dir = f"frames/{folder_name}/"
    await saveFrames(tmp_file_path, output_dir)
    zip_path = f"download/{folder_name}.zip"
    shutil.make_archive(f"download/{folder_name}", 'zip', output_dir)
    os.remove(tmp_file_path)
    shutil.rmtree(output_dir)
    
    return {'message': 'Done', 'folder': zip_path}

fapp.mount("/download", StaticFiles(directory="Framesio\Backend\download"), name="download")