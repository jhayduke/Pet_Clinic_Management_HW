from sqlalchemy import create_engine, import Integer, String,ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from datetime import datetime


Session = sessionmaker(bind=engine)
session = Session() 

engine = create_engine('sqlite:///pet_clinic_HW.db')


Base = declarative_base()

class Owner(Base):
    __tablename__ = 'Owners'
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    name: Mapped[String] = mapped_column(String(150), unique=True, nullable=False)
    phone:  Mapped[int] = mapped_column(String(25), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True)

class Pet(Base):
    __tablename__ = 'Pets'
    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    species: Mapped[str] = mapped_column(String(150), nullable=False)
    breed: Mapped[str] = mapped_column(String(150), nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, unique=True, ForeignKey('Owners.id'))

class Vet(Base):
    __tablename__ = 'Vets'
    id: Mapped[int] = mapped_column(Integer, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    specialization: Mapped[str] = mapped_column(String(250), nullable=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, Nullable=True)






Base.metadata.create_all(bind=engine)
