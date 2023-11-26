import pytest
from smallest_factor import smallest_factor
def test_smallest_factor():
    assert smallest_factor(25) == 5
def test_smallest_factor_even():
    assert smallest_factor(2) == 2

def test_smallest_factor_odd():
    assert smallest_factor(7) == 7

def test_smallest_factor_zero():
    assert smallest_factor(0) == 0

def test_smallest_factor_negative_num():
    with pytest.raises(ValueError) as e:
        smallest_factor(-10)
    assert "Input must be a non-negative integer." == e.value.args[0]



if __name__ == "__main__":
    pytest.main()