from pydantic import BaseModel,filed



class Voise(BaseModel):
    duration: int| float
    mime_type: str
    file_id: str
    file_unique_id: str
    file_size: int


class Audio(BaseModel):
    duration: int | float
    file_name: str
    mime_type: str
    title: str = None
    performer: str = None
    file_id: str
    file_unique_id: str
    file_size: int





class Answer(BaseModel):
    update_id: int = None
    message: int = None
