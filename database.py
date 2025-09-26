import sqlite3
import os
from datetime import datetime
from flask import g

DATABASE = 'coin_database.db'

def get_db():
    """데이터베이스 연결을 가져옵니다."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    """데이터베이스를 초기화합니다."""
    with sqlite3.connect(DATABASE) as conn:
        # 사용자 테이블
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 이안류 데이터 테이블
        conn.execute('''
            CREATE TABLE IF NOT EXISTS rip_current_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT NOT NULL,
                wave_height REAL,
                tide_level REAL,
                flux_value REAL,
                risk_level TEXT,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 드론 상태 테이블
        conn.execute('''
            CREATE TABLE IF NOT EXISTS drone_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drone_id TEXT NOT NULL,
                status TEXT NOT NULL,
                battery_level INTEGER,
                location_lat REAL,
                location_lng REAL,
                last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 알림 테이블
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT NOT NULL,
                message TEXT NOT NULL,
                notification_type TEXT,
                is_read BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # CCTV 영상 테이블
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cctv_videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                location TEXT,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                processed BOOLEAN DEFAULT FALSE
            )
        ''')
        
        conn.commit()

def close_db(error):
    """데이터베이스 연결을 닫습니다."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 샘플 데이터 삽입
def insert_sample_data():
    """샘플 데이터를 삽입합니다."""
    with sqlite3.connect(DATABASE) as conn:
        # 샘플 사용자 데이터
        conn.execute('''
            INSERT OR IGNORE INTO users (username, email, password_hash, role) 
            VALUES ('admin', 'admin@coin.com', 'admin123', 'admin')
        ''')
        
        # 샘플 이안류 데이터
        conn.execute('''
            INSERT OR IGNORE INTO rip_current_data 
            (location, wave_height, tide_level, flux_value, risk_level) 
            VALUES ('해운대해수욕장', 1.2, 150, 0.8, 'medium')
        ''')
        
        # 샘플 드론 데이터
        conn.execute('''
            INSERT OR IGNORE INTO drone_status 
            (drone_id, status, battery_level, location_lat, location_lng) 
            VALUES ('DRONE_001', 'active', 85, 35.1595, 129.1606)
        ''')
        
        conn.commit()

