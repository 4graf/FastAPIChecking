import logging_config
import logging
from database import Base, engine
import models

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
