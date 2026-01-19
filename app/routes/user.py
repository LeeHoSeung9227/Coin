from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)  # Blueprint 정의

@user_bp.route('/')
def user():
    return render_template('이용객.html')
