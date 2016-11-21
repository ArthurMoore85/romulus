"""
:module: database.py
:description: Database connection for Romulus

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 19/11/16
"""
from __future__ import unicode_literals
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


__author__ = 'arthur'

Base = declarative_base()


class Settings(Base):
    """
    Settings table
    """
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    download_location = Column(String)
    local_ip = Column(String)
    selected_service = Column(String)


class RetropieSettings(Base):
    """
    Retropie settings table
    """
    __tablename__ = 'retropie_settings'
    id = Column(Integer, primary_key=True)
    last_known_ip = Column(String)
    username = Column(String)
    password = Column(String)


class Product(Base):
    """
    Internal product settings
    """
    __tablename__ = 'product_settings'
    id = Column(Integer, primary_key=True)
    version_major = Column(Integer)
    version_minor = Column(Integer)
    version_patch = Column(Integer)
    release_date = Column(DateTime)

engine = create_engine('sqlite:///data/romulus-data')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
