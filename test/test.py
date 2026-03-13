import pytest
from src import sample_hello_world_script as hw


def setup_function(function):
    """Выполняется перед каждым тестом"""
    print(f"\nYou have called setUp() for {function.__name__}")


def teardown_function(function):
    """Выполняется после каждого теста"""
    print(f"You have called tearDown() for {function.__name__}")


# --- Тесты ---

def test_first_function_to_uppercase():
    input_value = 'Venkatt Guhesan'
    expected_result = 'VENKATT GUHESAN'
    actual_result = hw.first_function_to_uppercase(input_value)
    assert actual_result == expected_result


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']


def test_split_raises_type_error():
    s = 'hello world'
    with pytest.raises(TypeError):
        s.split(2)