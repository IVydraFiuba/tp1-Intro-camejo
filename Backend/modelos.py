from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Insumo(db.Model):
    __tablename__ = 'insumos'
    id = db.Column( db.Integer, primary_key=True, autoincrement=True )
    codigo = db.Column( db.String(255), unique=True, nullable=False )
    descripcion = db.Column( db.String(255), unique=True, nullable=False )
    presentacion = db.Column( db.String(255), nullable=False )
    rendimiento = db.Column( db.Integer, nullable=False)
