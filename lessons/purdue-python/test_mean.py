from stats import mean

def test_mean():
    assert mean([0, 0, 0, 0]) == 0
    assert mean([0, 200]) == 100
    assert mean([0, -200]) == -100
    assert mean([0]) == 0


def test_floating_mean():
    assert mean([1, 2]) == 1.5