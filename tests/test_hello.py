import pytest
from hello import hello

def test_hello_with_name():
    assert hello("Foo") == 'Hello, Foo!'

def test_hello_without_name():
    assert hello() == 'Hello!'
