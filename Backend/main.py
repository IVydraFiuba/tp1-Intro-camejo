from flask import Flask , request , jsonify
from flask_cors import CORS

from configuraciones import Desarrollo,Entrega
from modelos import db


app = Flask(__name__)
app.config.from_object(Desarrollo) 
CORS(app)

#aca vamos a manejar todas las rutas y a la mierda, HACE LO QUE VISTE EN CLASE 

if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()