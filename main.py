from fastapi import FastAPI, File, UploadFile
app = FastAPI()


@app.post("/upload")
def upload_file(file: UploadFile=File(...)):
    filename = file.filename
    if file:
        with open(f'./tmp/{filename}', 'wb') as f:
            [f.write(chunk) for chunk in iter(lambda: file.file.read(10240), b'')]
        return {
                    "message": "File Uploaded successfully",
                    "filename": filename
                }
    else:
        return {"message": "File Uploaded failed"}