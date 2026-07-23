from pydantic import BaseModel


class Transport(BaseModel):
    transport_number: str
    description: str
    owner: str
    status: str