from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session() #Create Sessions


engine = create_engine('sqlite:///clinic.db')

Base = declarative_base()

class Model(Base):
    __tablename__ = 'ids'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(str(150), unique=True, nullable=False)
    phone:  Mapped[int] = mapped_column(str(12), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(str(150), unique=True)