from flask import Flask , request , jsonify
from flask_cors import CORS

from configuraciones import Desarrollo,Entrega
from modelos import db , Insumo

app = Flask(__name__)
app.config.from_object(Desarrollo) 
CORS(app)

#aca vamos a manejar todas las rutas y a la mierda, HACE LO QUE VISTE EN CLASE 
@app.route('/')
def hello_world():
    return '<a href="/insumos">Ir a todos los insumos</a>', 200


@app.route('/insumos',methods=["GET"]) #Por defauld es GET pero no esta mal ponerlo
def data_insumos():
    try:
        insumos = Insumo.query.all()
        insumos_data=[]
        for insumo in insumos:
            insumo_data={
                'Id':insumo.id,
                'Codigo':insumo.codigo,
                'Descripcion':insumo.descripcion,
                'Presentacion': insumo.presentacion,
                'Rendimiento': insumo.rendimiento
            }
            insumos_data.append(insumo_data)
        return jsonify(insumos_data)
    except:
        return jsonify({"mensaje":"No tenemos insumos cargados"}),409

@app.route('/insumos', methods=["POST"])
def nuevo_insumo():
    try:
        data_formulario=request.json

        codigo_ingresado=data_formulario.get("codigo")
        descripcion_ingresada=data_formulario.get("descripcion")
        presentacion_ingresada=data_formulario.get("presentacion")
        rendimiento_ingresado=data_formulario.get("rendimiento")

        nuevo_insumo=Insumo(codigo=codigo_ingresado, descripcion=descripcion_ingresada, presentacion=presentacion_ingresada, rendimiento=rendimiento_ingresado)
        
        db.session.add(nuevo_insumo)
        db.session.commit()
        #Una buena practica es retornar lo que registramos
        return jsonify({'Insumo': {'Id':nuevo_insumo.id , 'Codigo':nuevo_insumo.codigo, 'Descripcion':nuevo_insumo.descripcion, 'Presentacion': nuevo_insumo.presentacion, 'Rendimiento': nuevo_insumo.rendimiento}})    
    
    except Exception as error:
        print(error)
        return jsonify({'message':'No se pudo cargar el insumo'}),500


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()