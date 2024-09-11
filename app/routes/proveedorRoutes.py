from flask import Blueprint, render_template, request, redirect, url_for
from app.models.proveedor import Proveedor
from app import db

bp = Blueprint('proveedorRoutes', __name__)

@bp.route('/proveedor')
def index():
    data = Proveedor.query.all()
    return render_template('proveedor/index.html', data=data)

@bp.route('/proveedor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        numero_telefono = request.form['numero_telefono']

        newProveedor = Proveedor(nombre=nombre, direccion=direccion, numero_telefono=numero_telefono)

        db.session.add(newProveedor)
        db.session.commit()

        return redirect(url_for('proveedorRoutes.index'))

    return render_template('proveedor/add.html')

@bp.route('/proveedor/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.direccion = request.form['direccion']
        proveedor.numero_telefono = request.form['numero_telefono']

        db.session.commit()

        return redirect(url_for('proveedorRoutes.index'))

    return render_template('proveedor/edit.html', proveedor=proveedor)

@bp.route('/proveedor/delete/<int:id>')
def delete(id):
    proveedor = Proveedor.query.get_or_404(id)

    db.session.delete(proveedor)
    db.session.commit()

    return redirect(url_for('proveedorRoutes.index'))
