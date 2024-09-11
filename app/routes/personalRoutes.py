from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.personal import Personal
from app import db

bp = Blueprint('personalRoutes', __name__)

@bp.route('/personals')
def index():
    personals = Personal.query.all()
    return render_template('personal/index.html', personals=personals)

@bp.route('/personals/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        hora_entrada = request.form['hora_entrada']
        hora_salida = request.form['hora_salida']

        newPersonal = Personal(nombre=nombre, hora_entrada=hora_entrada, hora_salida=hora_salida)

        db.session.add(newPersonal)
        db.session.commit()

        flash('Personal agregado exitosamente', 'success')
        return redirect(url_for('personalRoutes.index'))

    return render_template('personal/add.html')

@bp.route('/personals/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    personal = Personal.query.get_or_404(id)

    if request.method == 'POST':
        personal.nombre = request.form['nombre']
        personal.hora_entrada = request.form['hora_entrada']
        personal.hora_salida = request.form['hora_salida']

        db.session.commit()

        flash('Personal actualizado exitosamente', 'success')
        return redirect(url_for('personalRoutes.index'))

    return render_template('personal/edit.html', personal=personal)

@bp.route('/personals/delete/<int:id>')
def delete(id):
    personal = Personal.query.get_or_404(id)

    db.session.delete(personal)
    db.session.commit()

    flash('Personal eliminado exitosamente', 'success')
    return redirect(url_for('personalRoutes.index'))
