from fastapi import FastAPI, File, UploadFile, HTTPException
app = FastAPI()


@app.post("/upload")
def upload_file(file: UploadFile=File(...)):
    filename = file.filename
    try: 
        with open(f'./tmp/{filename}', 'wb') as f:
            [f.write(chunk) for chunk in iter(lambda: file.file.read(10240), b'')]
        return {
                    "message": "File Uploaded successfully",
                    "filename": filename
                }
    except:
        raise HTTPException(status_code=400, detail="File upload failed, did you include a file in your req?")