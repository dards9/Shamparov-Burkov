
import whisper
from fastapi import FastAPI,Request
import uvicorn

from schemas import Answer
from swh import Answer

model = whisper.load_model("small")
result = model.transcribe("./text.mp3")
print(result["text"])


app=FastAPI()
@app.post("/")
async def read_root(request:Request):
    json=await request.json()
    print(json)
    return 200



if __name__=="__main__":
    uvicorn.run("main:app",port=8000,host="0.0.0.0",reload=False)
    print ("fjdijdf")
