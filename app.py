from flask import Flask, render_template, request, redirect, url_for, jsonify
from modelos import db, Usuario, Marker

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route('/', methods=['POST', 'GET']) #Por defecto usa 'GET'
def index():
    if request.method == 'POST':
        correo_usuario = request.form.get('correo_usuario')
        password_usuario = request.form.get('password_usuario')
        user = Usuario.query.filter_by(correo_usuario=correo_usuario, password_usuario=password_usuario).first()
        print (user)
        if user != None:
            return redirect (url_for('conocenos'))
        else:
            return render_template('index.html', login_fallido=True)


    return render_template('index.html', login_fallido=False)

@app.route('/crear_cuenta', methods=['GET','POST'])
def crear_cuenta():
    
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        correo_usuario = request.form.get('correo_usuario')
        ciudad_usuario = request.form.get('ciudad_usuario')
        password_usuario = request.form.get('password_usuario')
        usuario = Usuario(nombre_usuario=nombre_usuario, correo_usuario=correo_usuario, ciudad_usuario=ciudad_usuario, password_usuario=password_usuario)

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear_cuenta.html')

@app.route ('/conocenos')
def conocenos ():
    return render_template('conocenos.html')


@app.route ('/actividades')
def eventos ():
    return render_template('actividades.html')


@app.route ('/recompensas')
def recompensas ():
    return render_template('recompensas.html')


@app.route ('/foro_comunitario')
def foro_comunitario ():
    return render_template('foro_comunitario.html')

#Rutas
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

#Pagina para guardar marcadores en la db
@app.route('/save_marker', methods=['POST'])
def save_marker():
    data = request.json
    new_marker = Marker(latitude=data['lat'], longitude=data['lng'], desafio=data['desafio'], descripcion=data['descripcion'], fecha_inicio=data['fecha_inicio'], fecha_termino=data['fecha_termino'])
    db.session.add(new_marker)
    db.session.commit()
    return jsonify({'status': 'success', 'id': new_marker.id})


#Pagina para leer marcadores de la db
@app.route('/get_markers', methods=['GET'])
def get_markers():
    markers = Marker.query.all()
    markers_data = [{"latitude": marker.latitude, "longitude": marker.longitude,'desafio': marker.desafio, 'descripcion': marker.descripcion, 'fecha_inicio': marker.fecha_inicio, 'fecha_termino': marker.fecha_termino, "id": marker.id} for marker in markers]
    return jsonify(markers_data)

@app.route('/eventos', methods=['GET'])
def actividades():
    marker = Marker.query.all()
    print(marker)
    return render_template('eventos.html', markers=marker)







if __name__ == '__main__':
    app.run(debug=True)