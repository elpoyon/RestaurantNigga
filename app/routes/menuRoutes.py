from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.menu import Menu
from app import db
from datetime import datetime

bp = Blueprint('menuRoutes', __name__)

@bp.route('/menus')
def index():
    menus = Menu.query.all()
    return render_template('menu/index.html', menus=menus)

@bp.route('/menus/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        sopa = request.form.get('sopa')
        proteinas = request.form.get('proteinas')
        principio_ensalada = request.form.get('principio_ensalada')
        bebidas = request.form.get('bebidas')
        usuario_id = request.form.get('usuario_id')

        newMenu = Menu(
            fecha=datetime.strptime(fecha, '%Y-%m-%d'),
            sopa=sopa,
            proteinas=proteinas,
            principio_ensalada=principio_ensalada,
            bebidas=bebidas,
            usuario_id=int(usuario_id)
        )
        try:
            db.session.add(newMenu)
            db.session.commit()
            flash('Menu agregado exitosamente', 'success')
        except:
            db.session.rollback()
            flash('Error al agregar el menu', 'danger')
        return redirect(url_for('menuRoutes.index'))

    return render_template('menu/add.html')

@bp.route('/menus/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    menu = Menu.query.get_or_404(id)
    
    if request.method == 'POST':
        menu.fecha = datetime.strptime(request.form.get('fecha'), '%Y-%m-%d')
        menu.sopa = request.form.get('sopa')
        menu.proteinas = request.form.get('proteinas')
        menu.principio_ensalada = request.form.get('principio_ensalada')
        menu.bebidas = request.form.get('bebidas')
        menu.usuario_id = int(request.form.get('usuario_id'))
        
        try:
            db.session.commit()
            flash('Menu actualizado exitosamente', 'success')
        except:
            db.session.rollback()
            flash('Error al actualizar el menu', 'danger')
        return redirect(url_for('menuRoutes.index'))

    return render_template('menu/edit.html', menu=menu)

@bp.route('/menus/delete/<int:id>')
def delete(id):
    menu = Menu.query.get_or_404(id)
    try:
        db.session.delete(menu)
        db.session.commit()
        flash('Menu eliminado exitosamente', 'success')
    except:
        db.session.rollback()
        flash('Error al eliminar el menu', 'danger')
    return redirect(url_for('menuRoutes.index'))
