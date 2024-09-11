from flask import Blueprint, render_template, request, redirect, url_for
from app.models.mercancia import Mercancia
from app.models.proveedor import Proveedor
from app import db

bp = Blueprint('mercanciaRoutes', __name__)

@bp.route('/mercancia')
def index():
    data = Mercancia.query.all()
    return render_template('mercancias/index.html', data=data)

@bp.route('/mercancia/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrepro = request.form['nombrepro']
        tipomer = request.form['tipomer']
        adenlace = request.form['adenlace']
        precio = request.form['precio']
        proveedor_id = request.form['proveedor_id']

        newMercancia = Mercancia(nombrepro=nombrepro, tipomer=tipomer, adenlace=adenlace, precio=precio, proveedor_id=proveedor_id)

        db.session.add(newMercancia)
        db.session.commit()

        return redirect(url_for('mercanciaRoutes.index'))

    proveedores = Proveedor.query.all()
    return render_template('mercancias/add.html', proveedores=proveedores)

@bp.route('/mercancia/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    mercancia = Mercancia.query.get_or_404(id)

    if request.method == 'POST':
        mercancia.nombrepro = request.form['nombrepro']
        mercancia.tipomer = request.form['tipomer']
        mercancia.adenlace = request.form['adenlace']
        mercancia.precio = request.form['precio']
        mercancia.proveedor_id = request.form['proveedor_id']

        db.session.commit()

        return redirect(url_for('mercanciaRoutes.index'))

    proveedores = Proveedor.query.all()
    return render_template('mercancias/edit.html', mercancia=mercancia, proveedores=proveedores)

@bp.route('/mercancia/delete/<int:id>')
def delete(id):
    mercancia = Mercancia.query.get_or_404(id)

    db.session.delete(mercancia)
    db.session.commit()

    return redirect(url_for('mercanciaRoutes.index'))
