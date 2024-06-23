from hello1 import hello


def test_default():
    assert hello() == "hello, world"


# having more test functions is more helpful
# but not too complicated that we have to test our tests
def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
