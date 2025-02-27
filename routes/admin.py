from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)  # Blueprint 정의

@admin_bp.route('/')
def admin():
    return render_template('관리자.html')
