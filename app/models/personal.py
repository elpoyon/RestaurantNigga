from app import db

class Personal(db.Model):
    __tablename__ = 'personals'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    hora_entrada = db.Column(db.Time, nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    ventas = db.relationship('Venta', back_populates='personal')
