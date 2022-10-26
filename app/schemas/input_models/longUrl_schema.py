from pydantic import BaseModel

class LongUrlInput(BaseModel):
    longUrl: str
