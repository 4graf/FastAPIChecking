from fastapi import APIRouter, Depends
from app.db.schemas import client
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.crud import crud_client

router = APIRouter()


@router.get('/', tags=['client'])
async def get_all(db: Session = Depends(get_db)):
    return crud_client.get_all_clients(db=db)


@router.get('/{id}', tags=['client'])
async def get(id_: int, db: Session = Depends(get_db)):
    return crud_client.get_client(id_=id_, db=db)


@router.post('/', tags=['client'])
async def create(data: client.ClientCreate, db: Session = Depends(get_db)):
    return crud_client.create_client(data=data, db=db)


@router.put('/{id}', tags=['client'])
async def update(id_: int, data: client.ClientCreate, db: Session = Depends(get_db)):
    return crud_client.update_client(id_=id_, data=data, db=db)


@router.delete('/{id}', tags=['client'])
async def update(id_: int, db: Session = Depends(get_db)):
    return crud_client.delete_client(id_=id_, db=db)
