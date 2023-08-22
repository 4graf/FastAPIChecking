from pydantic import BaseModel

from typing import Optional

from datetime import datetime


class ClientBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    # date_registration: Optional[datetime] = None


class ClientCreate(ClientBase):
    name: str
    email: str


class ClientUpdate(ClientBase):
    pass


class ClientDelete(ClientBase):
    pass


class ClientInDBBase(ClientBase):
    id: int

    class Config:
        from_attributes = True


class Client(ClientInDBBase):
    pass


class ClientInDB(ClientInDBBase):
    pass
