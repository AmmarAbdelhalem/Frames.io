import cv2
import os
import asyncio

async def saveFrames(file_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(file_path)
    success, image = vidcap.read()
    count = 0
    
    loop = asyncio.get_event_loop()
    
    while success:
        frame_path = os.path.join(output_dir, f"frame_{count:04d}.jpg")
        await loop.run_in_executor(None, cv2.imwrite, frame_path, image)
        success, image = vidcap.read()
        count += 1
    
    vidcap.release()
