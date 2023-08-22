from fastapi import FastAPI
import uvicorn
from app.db.database import Base, engine
from app.routers import client as client_router


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(client_router.router, prefix='/user')

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8080, reload=True, workers=3)
