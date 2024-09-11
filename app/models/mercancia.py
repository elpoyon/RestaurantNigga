from app import db

class Mercancia(db.Model):
    __tablename__ = 'mercancias'
    id = db.Column(db.Integer, primary_key=True)
    nombrepro = db.Column(db.String(255), nullable=False)
    tipomer = db.Column(db.String(255))
    adenlace = db.Column(db.String(255))
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    
    ventas = db.relationship('Venta', back_populates='mercancias')
    proveedor = db.relationship('Proveedor', back_populates='mercancias')
