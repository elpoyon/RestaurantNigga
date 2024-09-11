from app import db

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    sopa = db.Column(db.String(255))
    proteinas = db.Column(db.String(255))
    principio_ensalada = db.Column(db.String(255))
    bebidas = db.Column(db.String(255))
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='menus')
    ventas = db.relationship('Venta', back_populates='menu')
