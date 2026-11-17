from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

clase_recurso = db.Table(
    'clase_recurso',
    db.Column('clase_id', db.Integer, db.ForeignKey('clases.id'), primary_key=True),
    db.Column('recurso_id', db.Integer, db.ForeignKey('recursos.id'), primary_key=True)
)

class EspacioCurricular(db.Model):
    __tablename__ = 'espacios_curriculares'
    id = db.Column(db.Integer, primary_key=True)
    institucion = db.Column(db.String(120), nullable=False)
    materia = db.Column(db.String(120), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    turno = db.Column(db.String(30), nullable=False)
    ciclo_lectivo = db.Column(db.Integer, default=2026)
    unidades = db.relationship('Unidad', backref='espacio', cascade='all, delete-orphan', lazy=True)

class Unidad(db.Model):
    __tablename__ = 'unidades'
    id = db.Column(db.Integer, primary_key=True)
    espacio_id = db.Column(db.Integer, db.ForeignKey('espacios_curriculares.id'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    objetivos = db.Column(db.Text, nullable=True)
    contenidos = db.Column(db.Text, nullable=True)
    clases = db.relationship('Clase', backref='unidad', cascade='all, delete-orphan', lazy=True)

class Clase(db.Model):
    __tablename__ = 'clases'
    id = db.Column(db.Integer, primary_key=True)
    unidad_id = db.Column(db.Integer, db.ForeignKey('unidades.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=date.today)
    tema = db.Column(db.String(200), nullable=False)
    descripcion_actividad = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(30), default='Planificada') # Planificada | Dictada | Reprogramada
    recursos = db.relationship('Recurso', secondary=clase_recurso, lazy='subquery',
                               backref=db.backref('clases', lazy=True))

class Recurso(db.Model):
    __tablename__ = 'recursos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(30), nullable=False) # PDF | Enlace | Consigna
    ruta_o_url = db.Column(db.String(300), nullable=False)
    etiquetas = db.Column(db.String(150), nullable=True)