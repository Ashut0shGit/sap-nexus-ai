from pydantic import BaseModel

class SAPObject(BaseModel):
    object_name: str
    object_type: str
    description: str