import pytest


@pytest.mark.greetings
@pytest.mark.merhaba
@pytest.mark.hello
def test_fake_function1():
    print("hello1")
    assert True


@pytest.mark.greetings
@pytest.mark.hola
def test_fake_function2():
    print("hello2")
    assert True
