from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_usuario = db.Column(db.String(255), nullable=False)
    mercado_id = db.Column(db.Integer, db.ForeignKey('mercados.id'), nullable=False)
    plata = db.Column(db.Integer, nullable=False , default=500)
    dia = db.Column(db.Integer, nullable=False , default=1)

class Mercado(db.Model):
    __tablename__ = 'mercados'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_mercado = db.Column(db.String(255), nullable=False)
    licencias = db.Column(db.Integer, nullable=False , default=1)
    deuda_id = db.Column(db.Integer, db.ForeignKey('deudas.id'), nullable= False)

class Deuda(db.Model):
    __tablename__ = 'deudas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prestamo = db.Column(db.Integer, nullable=False , default=0)
    luz = db.Column(db.Integer, nullable=False , default=0)
    alquiler = db.Column(db.Integer, nullable=False , default=0)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_producto = db.Column(db.String(255), nullable=False, unique=True)
    tipo_producto = db.Column(db.String(255), nullable=False)
    precio_mercado = db.Column(db.Integer, nullable=False)

class Productos_usuario(db.Model):
    __tablename__ = 'Productos_usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad_prodcuto = db.Column(db.Integer, nullable=False)
    precio_venta = db.Column(db.Integer, nullable=False)

#sirve para que pueda importar usando el * enves de poner todos los nombres
__all__ = ['db', 'Usuario', 'Mercado', 'Deuda', 'Producto', 'Productos_usuario']