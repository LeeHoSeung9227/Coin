from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)  # Blueprint 정의

@home_bp.route('/')
def home():
    return render_template('index.html')
