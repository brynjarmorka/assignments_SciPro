import metutils


def test_f2c():
    assert metutils.f2c(9941) == 5505
    assert metutils.f2c(212) == 100
    assert metutils.f2c(32) == 0


def test_c2f():
    assert metutils.c2f(5505) == 9941
    assert metutils.c2f(100) == 212
    assert metutils.c2f(0) == 32
