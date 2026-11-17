from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import db, EspacioCurricular, Unidad, Clase, Recurso

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planifaula.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def dashboard():
    espacios = EspacioCurricular.query.all()
    proximas_clases = Clase.query.order_by(Clase.fecha.asc()).all()
    recursos = Recurso.query.all()
    total_dictadas = Clase.query.filter_by(estado='Dictada').count()
    return render_template(
        'dashboard.html',
        espacios=espacios,
        clases=proximas_clases,
        recursos=recursos,
        total_dictadas=total_dictadas
    )

@app.route('/espacio/nuevo', methods=['POST'])
def crear_espacio():
    nuevo = EspacioCurricular(
        institucion=request.form['institucion'],
        materia=request.form['materia'],
        curso=request.form['curso'],
        turno=request.form['turno']
    )
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/espacio/<int:espacio_id>')
def detalle_espacio(espacio_id):
    espacio = EspacioCurricular.query.get_or_404(espacio_id)
    recursos = Recurso.query.all()
    return render_template('materia_detalle.html', espacio=espacio, recursos=recursos)

@app.route('/unidad/nueva/<int:espacio_id>', methods=['POST'])
def crear_unidad(espacio_id):
    unidad = Unidad(
        espacio_id=espacio_id,
        numero=int(request.form['numero']),
        titulo=request.form['titulo'],
        objetivos=request.form.get('objetivos', ''),
        contenidos=request.form.get('contenidos', '')
    )
    db.session.add(unidad)
    db.session.commit()
    return redirect(url_for('detalle_espacio', espacio_id=espacio_id))

@app.route('/clase/nueva/<int:unidad_id>', methods=['POST'])
def crear_clase(unidad_id):
    unidad = Unidad.query.get_or_404(unidad_id)
    fecha_obj = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
    clase = Clase(
        unidad_id=unidad_id,
        fecha=fecha_obj,
        tema=request.form['tema'],
        descripcion_actividad=request.form.get('descripcion_actividad', '')
    )
    recurso_id = request.form.get('recurso_id')
    if recurso_id:
        rec = Recurso.query.get(int(recurso_id))
        if rec:
            clase.recursos.append(rec)
    db.session.add(clase)
    db.session.commit()
    return redirect(url_for('detalle_espacio', espacio_id=unidad.espacio_id))

@app.route('/clase/estado/<int:clase_id>/<nuevo_estado>')
def cambiar_estado_clase(clase_id, nuevo_estado):
    clase = Clase.query.get_or_404(clase_id)
    if nuevo_estado in ['Planificada', 'Dictada', 'Reprogramada']:
        clase.estado = nuevo_estado
        db.session.commit()
    return redirect(request.referrer or url_for('dashboard'))

@app.route('/recurso/nuevo', methods=['POST'])
def crear_recurso():
    recurso = Recurso(
        titulo=request.form['titulo'],
        tipo=request.form['tipo'],
        ruta_o_url=request.form['ruta_o_url'],
        etiquetas=request.form.get('etiquetas', '')
    )
    db.session.add(recurso)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)