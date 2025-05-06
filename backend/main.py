from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from parser import conver_ojousama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/convert")
def convert_text(req: TextRequest):
    converted = conver_ojousama(req.text)
    converted = converted.replace("。", "。\n")
    return {"result": converted}