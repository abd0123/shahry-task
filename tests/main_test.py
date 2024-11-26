import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import NationalId
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_response():
    # run post request to /validate-nid with body 
    response = client.post("/validate-nid", json=NationalId(national_id="30105108800853").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": True,
        "data": {
            "birth_date": "2001-05-10",
            "birth_governorate": "Foreign Country",
            "birth_date_serial": "0085",
            "gender": "Male",
        }
    }

def test_invalid_response_13_digit():
    response = client.post("/validate-nid", json=NationalId(national_id="3010510880085").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": False,
        "message": "National ID number must be exactly 14 digits"
    }
    
def test_invalid_response_invalid_birth_month():
    response = client.post("/validate-nid", json=NationalId(national_id="30113108800853").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": False,
        "message": "month must be in 1..12"
    }
def test_invalid_response_invalid_birth_day():
    response = client.post("/validate-nid", json=NationalId(national_id="30105338800853").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": False,
        "message": "day is out of range for month"
    }

def test_invalid_response_invalid_birth_governorate():
    response = client.post("/validate-nid", json=NationalId(national_id="30105108900853").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": False,
        "message": "Birth governorate code is not valid: 89"
    }
    
def test_invalid_response_invalid_gender():
    response = client.post("/validate-nid", json=NationalId(national_id="30105108800803").model_dump())
    assert response.status_code == 200
    assert response.json() == {
        "valid": False,
        "message": "Gender digit is not valid: 0"
    }