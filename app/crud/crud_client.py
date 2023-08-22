from app.db.schemas import client as client_sch
from app.db.models import Client as ClientModel
from app.crud.util import setattrs

from sqlalchemy.orm import Session


import logging

log = logging.getLogger(__name__)


def get_all_clients(db: Session):
    return db.query(ClientModel).all()


def get_client(id_: int, db: Session):
    return db.query(ClientModel).filter_by(id=id_).first()


def create_client(data: client_sch.ClientCreate, db: Session):
    client = ClientModel(**data.model_dump())
    try:
        db.add(client)
        db.commit()
        db.refresh(client)
    except Exception as exc:
        log.error(exc, exc_info=True)

    return client


def update_client(id_: int, data: client_sch.ClientCreate, db: Session):
    client = db.query(ClientModel).get(id_)
    setattrs(client, data.model_dump())

    try:
        db.add(client)
        db.commit()
        db.refresh(client)
    except Exception as exc:
        log.error(exc, exc_info=True)

    return client


def delete_client(id_: int, db: Session):
    db.query(ClientModel).filter_by(id=id_).delete()
    db.commit()

    return f'Client with id={id_} deleted successfully!'
