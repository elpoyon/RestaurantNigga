from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    numero_telefono = db.Column(db.String(20), nullable=False)
    mercancias = db.relationship('Mercancia', back_populates='proveedor')
