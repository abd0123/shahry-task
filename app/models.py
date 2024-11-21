from pydantic import BaseModel

class NationalId(BaseModel):
    national_id: str

class Resoponse(BaseModel):
    valid: bool

class InvalidResponse(Resoponse):
    valid: bool = False
    message: str

class NationalIdData(BaseModel):
    birth_date: str
    gender: str

class ValidResponse(Resoponse):
    valid: bool = True
    data: NationalIdData