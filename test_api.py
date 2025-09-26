import requests
import json

# API 테스트 스크립트
def test_api():
    base_url = "http://localhost:5000"
    
    print("=== API 테스트 시작 ===\n")
    
    # 1. 이안류 데이터 조회 테스트
    print("1. 이안류 데이터 조회 테스트")
    try:
        response = requests.get(f"{base_url}/api/rip-current-data")
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {response.json()}")
    except Exception as e:
        print(f"오류: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. 드론 상태 조회 테스트
    print("2. 드론 상태 조회 테스트")
    try:
        response = requests.get(f"{base_url}/api/drone-status")
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {response.json()}")
    except Exception as e:
        print(f"오류: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 3. 통계 데이터 조회 테스트
    print("3. 통계 데이터 조회 테스트")
    try:
        response = requests.get(f"{base_url}/api/statistics")
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {response.json()}")
    except Exception as e:
        print(f"오류: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 4. 회원가입 테스트
    print("4. 회원가입 테스트")
    try:
        test_user = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "test123",
            "role": "user"
        }
        response = requests.post(f"{base_url}/auth/register", json=test_user)
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {response.json()}")
    except Exception as e:
        print(f"오류: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 5. 로그인 테스트
    print("5. 로그인 테스트")
    try:
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        response = requests.post(f"{base_url}/auth/login", json=login_data)
        print(f"상태 코드: {response.status_code}")
        print(f"응답: {response.json()}")
    except Exception as e:
        print(f"오류: {e}")
    
    print("\n=== API 테스트 완료 ===")

if __name__ == "__main__":
    test_api()


