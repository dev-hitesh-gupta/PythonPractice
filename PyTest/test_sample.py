import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = {"check":"hello"}
        assert hasattr(x, "check")


# content of test_tmp_path.py
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0