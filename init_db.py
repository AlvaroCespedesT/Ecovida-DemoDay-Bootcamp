from flask import Flask
from modelos import db, Usuario

#instanciamos de la class flask usando el servidor app
app = Flask("app")

#Configuracion de las bases de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#inicializamos la base de datos
db.init_app(app)



# creamos base de datos vacia
with app.app_context():
     db.create_all()