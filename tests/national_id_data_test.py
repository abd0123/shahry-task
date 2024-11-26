import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from datetime import datetime
from utils.enums import Gender

from utils.national_id_data import (
    extract_birth_date,
    extract_birth_governorate,
    extract_birth_date_serial,
    extract_gender
)

def test_extract_birth_date():
    assert extract_birth_date("29901011234567") == "1999-01-01"
    assert extract_birth_date("30001011234567") == "2000-01-01"
    with pytest.raises(ValueError):
        extract_birth_date("30013011234567")  # Invalid date

def test_extract_birth_governorate():
    assert extract_birth_governorate("29901011234567") == "Dakahlia"
    assert extract_birth_governorate("29902010134567") == "Cairo"
    with pytest.raises(ValueError):
        extract_birth_governorate("29999015534567")  # Invalid governorate code

def test_extract_birth_date_serial():
    assert extract_birth_date_serial("29901011234567") == "3456"
    assert extract_birth_date_serial("30001011234567") == "3456"

def test_extract_gender():
    assert extract_gender("29901011234577") == Gender.MALE.value
    assert extract_gender("29901011234568") == Gender.FEMALE.value
    with pytest.raises(ValueError):
        extract_gender("29901011234500")  # Invalid gender digit