from pydantic import BaseModel,filed



class Voise(BaseModel):
    duration: int| float
    mime_type: str
    file_id: str
    file_unique_id: str
    file_size: str

class Answer(BaseModel):
    update_id:int=None