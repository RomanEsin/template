from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Float,
    Table
)

from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.types import UserDefinedType
from sqlalchemy import func

from Database.database import Base


class User(Base):
    __tablename__ = "testusers"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="asdf")
