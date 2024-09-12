from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

# Definir el usuario y contraseña únicos del administrador
admin_username = 'admin'  # Cambia esto por el nombre de usuario del admin
admin_password = 'cladeon3-Nico'  # Cambia esto por la contraseña del admin

@auth_bp.route('/index')
def index():
    return render_template('indice/index.html')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validamos si el username y password corresponden al admin
        if username == admin_username and password == admin_password:
            # Crear un usuario ficticio en la sesión, puede ser un objeto o solo un valor simple
            admin_user = Usuario(id=1, correo=admin_username)  # Simulamos un usuario 'Usuario' con ID 1
            login_user(admin_user)  # Inicia sesión
            flash("Login successful!", "success")
            return redirect(url_for('auth.dashboard'))
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    # Si el usuario ya está autenticado, redirigir al dashboard
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    
    return render_template("login/login.html")

# Vista protegida solo para el administrador (dashboard)
@auth_bp.route('/index')
@login_required
def dashboard():
    return render_template('indice/index.html', user=current_user)

# Ruta para cerrar sesión
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
