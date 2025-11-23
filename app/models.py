from pydantic import BaseModel

class URLItem(BaseModel):
    original_url: str
