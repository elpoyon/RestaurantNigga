from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/index')
def index():
    return render_template('indice/index.html')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = Usuario.query.filter_by(correo=username, contraseña=password).first()

        if user:
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('auth.index')) 
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return render_template("login/login.html")

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.correo}! This is your dashboard.'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
