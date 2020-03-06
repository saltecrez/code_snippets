#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "December 2019"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class AFO(Base):
    __tablename__ = 'AFO'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255))
    storage_path = Column(String(255))
    file_path = Column(String(255))
    file_version = Column(Integer())

    def __init__(self, file_name, storage_path, file_path, file_version):
        self.file_name = file_name
        self.storage_path= storage_path
        self.file_path = file_path
        self.file_version = file_version

class ECH(Base):
    __tablename__ = 'ECH'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255))
    storage_path = Column(String(255))
    file_path = Column(String(255))
    file_version = Column(Integer())

    def __init__(self, file_name, storage_path, file_path, file_version):
        self.file_name = file_name
        self.storage_path= storage_path
        self.file_path = file_path
        self.file_version = file_version

class SBI(Base):
    __tablename__ = 'SBI'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(255))
    storage_path = Column(String(255))
    file_path = Column(String(255))
    file_version = Column(Integer())

    def __init__(self, file_name, storage_path, file_path, file_version):
        self.file_name = file_name
        self.storage_path= storage_path
        self.file_path = file_path
        self.file_version = file_version

