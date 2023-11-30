from flask_sqlalchemy import SQLAlchemy

#instanciamos la base de datos

db = SQLAlchemy()

#Creamos nuestro modelo de base de datos

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(40),nullable = False) #Debe ser nombre y apellido
    correo_usuario = db.Column(db.String (40),nullable = False)
    ciudad_usuario = db.Column(db.String (40), nullable = False)
    password_usuario = db.Column(db.String(40))

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    desafio = db.Column(db.String(200))
    descripcion = db.Column(db.String(400))
    fecha_inicio = db.Column(db.String(200))
    fecha_termino = db.Column(db.String(200))