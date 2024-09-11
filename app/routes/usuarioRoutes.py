from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.usuario import Usuario
from app import db

bp = Blueprint('usuarioRoutes', __name__)

@bp.route('/usuarioRoutes')
def index():
    data = Usuario.query.all()
    return render_template('usuario/index.html', data=data)

@bp.route('/usuarioRoutes/add', methods=['GET', 'POST'])
def add_usuario():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        newUsuario = Usuario(correo=correo, contraseña=contraseña)

        db.session.add(newUsuario)
        db.session.commit()

        flash('Usuario agregado exitosamente', 'success')
        return redirect(url_for('usuarioRoutes.index'))

    return render_template('usuario/add.html')
