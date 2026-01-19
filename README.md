# COIN - 해양 안전 정보 전달 서비스
지인의 프로젝트를 확장·정리한 **2인 팀** 웹 서비스로, 해수욕장 안전 정보를 역할별(관리자/안전요원/이용객/해양스포츠 애호가/어촌 주민/환경운동가)로 전달합니다.

## 프로젝트 개요
- 이안류 등 위험 요소를 시각화하고, 역할별로 필요한 정보를 빠르게 제공하는 웹 서비스
- Flask 기반 서버 + 정적 페이지 중심의 UI 구성

## 주요 기능
- **역할별 페이지 제공**: 관리자 / 안전요원 / 이용객 / 스포츠애호가 / 어촌주민 / 환경운동가
- **실시간 해양 정보 조회**: KHOA API 기반 파고/조위 정보 (lifeguard 라우트)
- **시각화 중심 메인 페이지**: 이미지/영상 기반 서비스 설명
- **반응형 UI 개선**: 주요 페이지 모바일/태블릿 대응

## 기술 스택
- **Backend**: Python, Flask, flask-cors
- **Frontend**: HTML/CSS, Vanilla JS
- **Data**: SQLite

## 폴더 구조
```
Coin/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── routes/               # Blueprint 라우트
│   ├── static/               # 정적 파일 (images, js, videos)
│   ├── templates/            # HTML 템플릿
│   └── database.py           # DB 유틸
├── data/                     # DB 파일
├── scripts/                  # 유틸 스크립트
├── tests/                    # 테스트
├── app.py                    # 실행 엔트리
└── wsgi.py                   # 배포 엔트리
```

## 실행 방법
```bash
# 1) 설치
pip install -r requirements.txt

# 2) 실행
python app.py
```

## 참고
- `/lifeguard/get_wave_and_tide_data`에서 파고/조위 데이터를 조회합니다.
- 일부 페이지는 소개용 템플릿으로 구성되어 있으며, 기능 확장 대상입니다.
