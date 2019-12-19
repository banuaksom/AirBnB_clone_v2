#!/usr/bin/python3
"""
Script will determine which database method to use based on input
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.dbstorage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
