from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from datetime import datetime


session = Session() 
Session = sessionmaker(bind=engine)

engine = create_engine('sqlite:///pet_clinic_HW.db')


Base = declarative_base()

class Owner(Base):
    __tablename__ = 'Owners'
    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[String] = mapped_column(str(150), unique=True, nullable=False)
    phone:  Mapped[int] = mapped_column(str(12), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(str(150), unique=True)

class Pet(Base):
    __tablename__ = 'Pets'
    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    species: Mapped[str] = mapped_column(String(150), nullable=False)
    breed: Mapped[str] = mapped_column(str, nullable=False)
    owner_id: Mapped[int] = mapped_column(int(150), unique=Tre, ForeignKey=True)

class Vet(Base):
    __tablename__ = 'Vets'
    id: Mapped[int] = mapped_column(int(150), unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(str(150), unique=True, nullable=False)
    specialization: Mapped[str] = mapped_column(str(250), nullable=True)
    email: Mapped[str] = mapped_column(str(150), unique=True, Nullable=True)






    Base.metadata.create_all(bind=engine)
