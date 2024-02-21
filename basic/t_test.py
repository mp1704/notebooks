import t
import pytest

# def test_square():
#     assert t.square(5) == 25
    
@pytest.mark.parametrize(
    "input, expected",
    [
      (3., 9.),
      (5., 25.)  
    ] 
)
def test_square_float(input, expected):
    assert t.square(input) == expected
    
# -v -s
