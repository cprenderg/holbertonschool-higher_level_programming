#!/usr/bin/python3

"""
Makes a model class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class City(Base):
    """
    Represents a city in the database.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
