import whisper
from fastapi import FastAPI,Request
import uvicorn
import aiophht

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
    odj=Answer.model_viledate(json) 

    file_id = odj.message.voise.file_id
    
    'https://api.telegram.org/bot{TG_API}/getFile'
    data={'file_id': file_id}
     
    async with aiophht.ClientSession() as session:
    



    return 200

    
