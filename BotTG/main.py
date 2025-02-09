import whisper
from fastapi import FastAPI,Request
import uvicorn
import aiohttp
import aiofiles
TG_API='7790178826:AAHzJIiCi9i6nS2-4xIqm74K6CuAcSPcJuY'


from schemas import Answer


model = whisper.load_model("small")
result = model.transcribe("./text.mp3")
print(result["text"])


app=FastAPI()
@app.post("/")
async def read_root(request:Request):
    json=await request.json()
    #print(json)
    odj=Answer.model_validate(json) 

    file_id = odj.message.voise.file_id

    data={'file_id': file_id}
     
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://api.telegram.org/bot{TG_API}/getFile', data= data) as reponse:
          resfileinfo=await reponse.json() 
          print(resfileinfo)
          if resfileinfo.get('ok'):
            path=resfileinfo['result']['file_path']
            ext = path.split('.')[-1]
            async with session.get(f'https://api.telegram.org/file/bot{TG_API}/{path}') as dwfile:
                async with aiofiles.open('filename',mode='wb') as f :
                   content=await dwfile.read()
                   await f.write(content)












    return 200
    
