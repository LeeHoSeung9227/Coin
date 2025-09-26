import sqlite3
from datetime import datetime

def insert_sample_data():
    conn = sqlite3.connect('coin_database.db')
    cursor = conn.cursor()
    
    # 기존 데이터 삭제
    cursor.execute('DELETE FROM users')
    cursor.execute('DELETE FROM rip_current_data')
    cursor.execute('DELETE FROM drone_status')
    cursor.execute('DELETE FROM notifications')
    cursor.execute('DELETE FROM cctv_videos')
    
    # 샘플 사용자 데이터
    cursor.execute('''
        INSERT INTO users (username, email, password_hash, role) 
        VALUES ('admin', 'admin@coin.com', 'scrypt:32768:8:1$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4Qj4Qj4Qj4', 'admin')
    ''')
    
    # 샘플 이안류 데이터
    cursor.execute('''
        INSERT INTO rip_current_data 
        (location, wave_height, tide_level, flux_value, risk_level) 
        VALUES ('해운대해수욕장', 1.2, 150, 0.8, 'medium')
    ''')
    
    cursor.execute('''
        INSERT INTO rip_current_data 
        (location, wave_height, tide_level, flux_value, risk_level) 
        VALUES ('해운대해수욕장', 0.8, 120, 0.5, 'low')
    ''')
    
    cursor.execute('''
        INSERT INTO rip_current_data 
        (location, wave_height, tide_level, flux_value, risk_level) 
        VALUES ('해운대해수욕장', 2.1, 180, 1.2, 'high')
    ''')
    
    # 샘플 드론 데이터
    cursor.execute('''
        INSERT INTO drone_status 
        (drone_id, status, battery_level, location_lat, location_lng) 
        VALUES ('DRONE_001', 'active', 85, 35.1595, 129.1606)
    ''')
    
    cursor.execute('''
        INSERT INTO drone_status 
        (drone_id, status, battery_level, location_lat, location_lng) 
        VALUES ('DRONE_002', 'charging', 25, 35.1595, 129.1606)
    ''')
    
    # 샘플 알림 데이터
    cursor.execute('''
        INSERT INTO notifications 
        (user_id, title, message, notification_type) 
        VALUES (1, '이안류 위험도 증가', '해운대해수욕장에서 이안류 위험도가 높음으로 감지되었습니다.', 'warning')
    ''')
    
    cursor.execute('''
        INSERT INTO notifications 
        (user_id, title, message, notification_type) 
        VALUES (NULL, '시스템 점검', '정기 시스템 점검이 완료되었습니다.', 'info')
    ''')
    
    conn.commit()
    conn.close()
    
    print("샘플 데이터가 성공적으로 삽입되었습니다!")

if __name__ == "__main__":
    insert_sample_data()


