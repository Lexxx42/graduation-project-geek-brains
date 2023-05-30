# content of test_indirect_list.py

import pytest


@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["y"])
def test_indirect(x, y):
    print(x)
    print(y)
    assert x == "aaa"
    assert y == "b"
