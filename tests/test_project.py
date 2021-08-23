import sys
from os import path
sys.path.append("./")
from src.utils import *
from src.constexpr import *
import pytest

def test_verify_password_length():
    assert len(password_generator()) == 10

def test_verify_password_strength():
    test_password = password_generator()
    print(test_password)
    score = 0
    for elem in test_password:
        print(score)
        print(elem)
        if elem in LOWERCASE:
            score += 5
        elif elem in UPPERCASE:
            score += 8
        elif elem in NUMBERS:
            score += 10
        elif elem in SPECIAL_CHAR:
            score += 15
    if string_uniqueness(test_password) >= 5:
        score += 20
    assert score >= 100

def test_my_data_is_created_and_data_is_written():
    dummy_website = "example@something.com"
    dummy_password = "123456iswrong"
    string_in_file = dummy_website + ' : ' + dummy_password
    store_login_data(dummy_website, dummy_password, True)
    file_exist = path.isfile(DUMMY_DATA)
    with open(DUMMY_DATA, 'r') as file:
            content = file.read()
    file_correct_content = string_in_file in content
    print(string_in_file + '   ' + content)
    assert file_exist
    assert file_correct_content
    os.remove(DUMMY_DATA)