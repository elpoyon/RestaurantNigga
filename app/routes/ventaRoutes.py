from flask import Blueprint, render_template, request, redirect, url_for
from app.models.venta import Venta
from app.models.usuario import Usuario
from app.models.menu import Menu
from app.models.personal import Personal
from app.models.mercancia import Mercancia  
from app import db

bp = Blueprint('ventaRoutes', __name__)

@bp.route('/venta')
def index():
    data = Venta.query.all()
    return render_template('venta/index.html', data=data)

@bp.route('/venta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        area = request.form['area']
        descripcion_corta = request.form['descripcion_corta']
        precio = request.form['precio']
        usuario_id = request.form['usuario_id']
        menu_id = request.form['menu_id']
        personal_id = request.form['personal_id']
        mercancia_id = request.form['mercancia_id']  

        newVenta = Venta(
            area=area,
            descripcion_corta=descripcion_corta,
            precio=precio,
            usuario_id=usuario_id,
            menu_id=menu_id,
            personal_id=personal_id,
            mercancia_id=mercancia_id  
        )

        db.session.add(newVenta)
        db.session.commit()

        return redirect(url_for('ventaRoutes.index'))

    usuarios = Usuario.query.all()
    menus = Menu.query.all()
    personals = Personal.query.all()
    mercancias = Mercancia.query.all() 
    return render_template('venta/add.html', usuarios=usuarios, menus=menus, personals=personals, mercancias=mercancias)

@bp.route('/venta/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    venta = Venta.query.get_or_404(id)

    if request.method == 'POST':
        venta.area = request.form['area']
        venta.descripcion_corta = request.form['descripcion_corta']
        venta.precio = request.form['precio']
        venta.usuario_id = request.form['usuario_id']
        venta.menu_id = request.form['menu_id']
        venta.personal_id = request.form['personal_id']
        venta.mercancia_id = request.form['mercancia_id']  

        db.session.commit()

        return redirect(url_for('ventaRoutes.index'))

    usuarios = Usuario.query.all()
    menus = Menu.query.all()
    personals = Personal.query.all()
    mercancias = Mercancia.query.all()  
    return render_template('venta/edit.html', venta=venta, usuarios=usuarios, menus=menus, personals=personals, mercancias=mercancias)

@bp.route('/venta/delete/<int:id>')
def delete(id):
    venta = Venta.query.get_or_404(id)

    db.session.delete(venta)
    db.session.commit()

    return redirect(url_for('ventaRoutes.index'))
