from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)  # Blueprint 정의

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/환경운동가')
def environmentalist():
    return render_template('환경운동가.html')

@home_bp.route('/어촌주민')
def fisherman():
    return render_template('어촌주민.html')

@home_bp.route('/관리자')
def admin_page():
    return render_template('관리자.html')

@home_bp.route('/안전요원')
def lifeguard_page():
    return render_template('안전요원.html')

@home_bp.route('/이용객')
def beachgoers():
    return render_template('이용객.html')

@home_bp.route('/스포츠애호가')
def marinesports():
    return render_template('스포츠애호가.html')