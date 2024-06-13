from main import app
from flask_sqlalchemy import SQLAlchemy
"""
Aca vamos a modelar las tablas de la base de datos.
La idea es que vamos a crear las clases con las que SQLAlchemy va a armar las tablas
"""
db=SQLAlchemy(app)

