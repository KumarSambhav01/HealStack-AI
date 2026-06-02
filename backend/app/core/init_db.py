from backend.app.core.database import engine, Base

# Import models here
from backend.app.models.incident import Incident


def init_db():
    Base.metadata.create_all(bind=engine)