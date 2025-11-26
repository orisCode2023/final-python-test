from fastapi import FastAPI, File, HTTPException, UploadFile
from controller import *

controller = Controller()

app = FastAPI()

@app.post("/assignWithCsv")
def upload_csv():
    assign = controller.assign_soldiers()
    return {assign}
