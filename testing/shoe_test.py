import pytest
from lib.shoe import Shoe  # Assuming your Shoe class is defined in a module named 'shoe'


def test_shoe_string_representation():
    # Test if the __str__ method returns the correct string representation
    shoe = Shoe("Nike", 9.5, "sneaker", "white", 99.99)
    expected_string = "Nike sneaker (size 9.5, white) - $99.99"
    assert str(shoe) == expected_string

def test_shoe_attributes():
    # Test if the shoe attributes are assigned correctly
    shoe = Shoe("Adidas", 10.0, "sandal", "black", 79.99)
    assert shoe.brand == "Adidas"
    assert shoe.size == 10.0
    assert shoe.style == "sandal"
    assert shoe.color == "black"
    assert shoe.price == 79.99
