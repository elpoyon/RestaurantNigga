from app import db

class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(255), nullable=False)
    descripcion_corta = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    personal_id = db.Column(db.Integer, db.ForeignKey('personals.id'), nullable=False)
    mercancia_id=db.Column(db.Integer,db.ForeignKey('mercancias.id'),nullable=False)
    
    usuario = db.relationship('Usuario', back_populates='ventas')
    menu = db.relationship('Menu', back_populates='ventas')
    personal = db.relationship('Personal', back_populates='ventas')
    mercancias = db.relationship('Mercancia', back_populates='ventas')
