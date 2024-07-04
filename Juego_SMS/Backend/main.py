from flask import Flask , request , jsonify
from flask_cors import CORS

from configuracion import Desarrollo,Entrega
from modelos import *

app = Flask(__name__)
app.config.from_object(Desarrollo) 
CORS(app)


@app.route('/',methods=["GET"])
def hello_world():
    return '<h1>Bienvenido a Super mercado Simulation</h1>', 200



@app.route('/Inicio/usuarios',methods=["GET"]) #Por defauld es GET pero no esta mal ponerlo
def data_usuarios():
    try:
        usuarios = Usuario.query.all()
        
        usuarios_data=[]
        for usuario in usuarios:
            mercado = Mercado.query.get(usuario.mercado_id)
            deuda = Deuda.query.get(mercado.deuda_id)
            usuario_data={
                'Id':usuario.id ,
                        'Nombre':usuario.nom_usuario,
                        'Mercado':{'Id': usuario.id,
                                    'Nombre': mercado.nom_mercado,
                                    'Licencias': mercado.licencias, 
                                    'Deuda':{'Id':deuda.id, 
                                            'Prestamo':deuda.prestamo, 
                                            'Luz': deuda.luz, 
                                            'alquiler': deuda.alquiler }},
                        'plata': usuario.plata, 
                        'dia': usuario.dia
            }
            usuarios_data.append(usuario_data)
        return jsonify(usuarios_data)
    except:
        return jsonify({'success':False,"mensaje":"No tenemos usuarios cargados"}),409


@app.route('/Inicio', methods=["POST"])
def nueva_partida():
    try:
        formulario_data =request.json
        Nom_usuario = formulario_data.get("nom_usuario")
        Nom_mercado = formulario_data.get("nom_mercado")
        #Aca si es necesario podria hacer validaciones de los datos que me paso el usuario
        #
        #
        nueva_deuda = Deuda()
        db.session.add(nueva_deuda)
        db.session.flush()

        nuevo_mercado = Mercado(nom_mercado=Nom_mercado, deuda_id=nueva_deuda.id)
        db.session.add(nuevo_mercado)
        db.session.flush()

        nuevo_usuario = Usuario(nom_usuario=Nom_usuario, mercado_id=nuevo_mercado.id)
        db.session.add(nuevo_usuario)
        db.session.commit()

        #Una buena practica es retornar lo que registramos
        return jsonify({
            'success':True,
            'Usuario':{'Id':nuevo_usuario.id ,
                        'Nombre':nuevo_usuario.nom_usuario,
                        'Mercado':{'Id': nuevo_mercado.id,
                                    'Nombre': nuevo_mercado.nom_mercado,
                                    'Licencias': nuevo_mercado.licencias, 
                                    'Deuda':{'Id':nueva_deuda.id, 
                                            'Prestamo':nueva_deuda.prestamo, 
                                            'Luz': nueva_deuda.luz, 
                                            'alquiler': nueva_deuda.alquiler }},
                        'plata': nuevo_usuario.plata, 
                        'dia': nuevo_usuario.dia}
                        })    
    except Exception as error:
        print(error)
        db.session.rollback()
        return jsonify({'success':False,'message':'No se pudo crear el usuario'}),500



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()