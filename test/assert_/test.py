

def assert_test(x):
    assert x >= 0, 'Число не должно быть отрицательным'
    return x

assert_test(1)
assert_test(0)
assert_test(-1)
assert_test(100)
