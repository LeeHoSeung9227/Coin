from flask import Flask, render_template
from flask_cors import CORS  # CORS 설정 추가
from routes.home import home_bp
from routes.admin import admin_bp
from routes.user import user_bp
from routes.lifeguard import lifeguard_bp

app = Flask(__name__)

# CORS 활성화
CORS(app)

# Blueprint 등록
app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(lifeguard_bp, url_prefix='/lifeguard')

@app.route('/')
def home():
    return render_template('index.html')

# 개별 페이지 라우트 추가
@app.route('/환경운동가')
def environmentalist():
    return render_template('환경운동가.html')

@app.route('/어촌주민')
def fisherman():
    return render_template('어촌주민.html')

@app.route('/관리자')
def admin():
    return render_template('관리자.html')

@app.route('/안전요원')
def lifeguard():
    return render_template('안전요원.html')

@app.route('/이용객')
def beachgoers():
    return render_template('이용객.html')

@app.route('/스포츠애호가')
def marinesports():
    return render_template('스포츠애호가.html')



if __name__ == '__main__':
    app.run(debug=True)
