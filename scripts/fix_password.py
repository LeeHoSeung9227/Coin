import os
import sqlite3
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(BASE_DIR, 'data', 'coin_database.db')

def fix_admin_password():
    # 올바른 비밀번호 해시 생성
    password_hash = generate_password_hash('admin123')
    print(f"새 비밀번호 해시: {password_hash}")
    
    # 데이터베이스 업데이트
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE users 
        SET password_hash = ? 
        WHERE username = 'admin'
    ''', (password_hash,))
    
    conn.commit()
    conn.close()
    
    print("관리자 비밀번호가 업데이트되었습니다!")

if __name__ == "__main__":
    fix_admin_password()


