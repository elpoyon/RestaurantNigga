from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(255), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    
    menus = db.relationship('Menu', back_populates='usuario')
    ventas = db.relationship('Venta', back_populates='usuario')
