from flask import render_template
from . import main
from app.models import User, Role

@main.route('/')
def index():
    if not current_user.is_anonymous:
        usuarios = User.query.all()
        return render_template('index.html', usuarios=usuarios, user=User, role=Role)
    else:
        return render_template('index.html')
