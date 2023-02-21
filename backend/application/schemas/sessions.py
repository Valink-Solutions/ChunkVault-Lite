from pydantic import BaseModel

class UploadSessionSchema(BaseModel):
    upload_id: str
    filename: str
    last_byte: int