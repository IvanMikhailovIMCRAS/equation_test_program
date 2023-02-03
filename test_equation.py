from equation import eq
import pytest

def test_eq():
    assert eq(1., 1., 1.) == 0.
    with pytest.raises(Exception) as error:
        eq(1., 1., -1.)
    assert str(error.value) == "there is no solution"
    
    with pytest.raises(Exception) as error:
        eq(0., 2., 1.)
    assert str(error.value) == "there is no solution"

    with pytest.raises(Exception) as error:
        eq(0., 4., 2.)
    assert str(error.value) == "many solutions"