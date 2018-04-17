import pytest

pytest_plugins = ['helpers_namespace']


@pytest.helpers.register
def assert_lines(expected, observed):
    e = [str(string) for string in expected]
    o = [str(string) for string in observed]
    e.sort()
    o.sort()
    assert e == o