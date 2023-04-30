import main


def test_it_should_work():
    assert True


def test_it_should_import_from_main():
    assert 2 == main.fun1(1)
    assert 3 == main.fun2(1)
