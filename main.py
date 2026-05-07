from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    owner_name = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    db = SessionLocal()
    pets = db.query(Pet).order_by(Pet.id.desc()).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "pets": pets})


@app.post("/add")
async def add_pet(
    request: Request,
    name: str = Form(...),
    weight: float = Form(...),
    age: int = Form(...),
    owner_name: str = Form(...),
):
    db = SessionLocal()
    pet = Pet(name=name.strip(), weight=weight, age=age, owner_name=owner_name.strip())
    db.add(pet)
    db.commit()
    db.refresh(pet)
    db.close()
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)