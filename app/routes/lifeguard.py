from flask import Flask, render_template, jsonify, Blueprint
import requests
from datetime import datetime, timedelta
import logging


lifeguard_bp = Blueprint('lifeguard', __name__)  # Blueprint 정의
logging.basicConfig(level=logging.DEBUG)

 
# 캐시 변수
cached_data = None
last_fetch_time = None
CACHE_DURATION = timedelta(minutes=20)

def get_wave_and_tide_info(api_key, obs_code="DT_0042"):
    global cached_data, last_fetch_time
    
    current_time = datetime.now()
    
    # 캐시된 데이터가 있고, 캐시 기간이 지나지 않았다면 캐시된 데이터 반환
    if cached_data and last_fetch_time and (current_time - last_fetch_time) < CACHE_DURATION:
        logging.debug("Returning cached data")
        return cached_data

    date = current_time.strftime("%Y%m%d")

    wave_url = "http://www.khoa.go.kr/api/oceangrid/obsWaveHight/search.do"
    tide_url = "http://www.khoa.go.kr/api/oceangrid/tideObs/search.do"
    
    params = {
        "ServiceKey": api_key,
        "ObsCode": obs_code,
        "Date": date,
        "ResultType": "json"
    }

    logging.debug("Fetching new data from API")
    try:
        wave_response = requests.get(wave_url, params=params, timeout=10)
        tide_response = requests.get(tide_url, params=params, timeout=10)
        
        wave_response.raise_for_status()
        tide_response.raise_for_status()
        
        wave_data = wave_response.json()
        tide_data = tide_response.json()

        wave_list = wave_data.get("result", {}).get("data", [])
        tide_list = tide_data.get("result", {}).get("data", [])

        latest_wave = wave_list[-1] if wave_list else None
        latest_tide = tide_list[-1] if tide_list else None

        result = {
            "wave_height": latest_wave.get("wave_height", "N/A") if latest_wave else "N/A",
            "wave_time": latest_wave.get("record_time", "N/A") if latest_wave else "N/A",
            "tide_level": latest_tide.get("tide_level", "N/A") if latest_tide else "N/A",
            "tide_time": latest_tide.get("record_time", "N/A") if latest_tide else "N/A",
            "fetch_time": current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 캐시 업데이트
        cached_data = result
        last_fetch_time = current_time
        
        logging.debug(f"New data fetched and cached: {result}")
        return result
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": f"데이터를 가져오는 데 실패했습니다: {str(e)}"}


# 라우트 설정 (Blueprint 사용)
@lifeguard_bp.route('/')
def index():
    return render_template('안전요원.html')  # 기존 index.html → lifeguard.html로 변경

@lifeguard_bp.route('/get_wave_and_tide_data')
def get_wave_and_tide_data():
    api_key = "gTXRwl5OEquWYCRwyrcKA=="  # 실제 API 키
    data = get_wave_and_tide_info(api_key)
    return jsonify(data)