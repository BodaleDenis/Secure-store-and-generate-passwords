import sys
sys.path.append("./")
from src.utils import *
import pytest

def test_verify_password_length():
    assert len(password_generator()) == 10

def test_sample():
    silly = True
    assert silly