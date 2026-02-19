import pytest
from src.utils import get_system_health
from src.validator import validate_user_payload
from src.calculator import process_payment

def test_system_health():
    assert get_system_health()["status"] == "healthy"

def test_validation():
    assert validate_user_payload({"username": "admin"}) == True

def test_payment():
    assert process_payment(100.0, 0.05) == "Total Paid: $105.0"
