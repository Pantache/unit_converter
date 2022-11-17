import pytest
from pytest import approx
from unit_converter import temp_conversion, length_conversion, mass_conversion

def test_temp_conversion():
    """Test if the temp_conversion function works correctly.
    Parameters: None
    Return: None
    """
    assert temp_conversion(0, "C°","F°") == approx(32.0)
    assert temp_conversion(0, "K°","F°") == approx(-459.67)
    assert temp_conversion(0, "F°","K°") == approx(255.372)
    assert temp_conversion(0, "C°","K°") == approx(273.15)
    assert temp_conversion(122, "F°","C°") == approx(50) 
    assert temp_conversion(32, "F°", "F°") == approx(32.0)
    assert temp_conversion(0, "","") == "Value Incorrect or not found"
    assert temp_conversion(5, "","F°") == "Value Incorrect or not found"
    assert temp_conversion(26, "C°","") == "Value Incorrect or not found"
    assert temp_conversion(0, "E°","") == "Value Incorrect or not found"
    assert temp_conversion("4", 0, 1) == "Value Incorrect or not found"
    assert temp_conversion(60, "K°", 2) == "Value Incorrect or not found"
    assert temp_conversion(60, 2, "C°") == "Value Incorrect or not found"
    assert temp_conversion("asdf", "K°", "C°") == "Value Incorrect or not found"
    assert temp_conversion(45, "c°", "K°") == "Value Incorrect or not found"

def test_lenght_conversion():
    """Test if the lenght_conversion function works correctly.
    Parameters: None
    Return: None
    """
    assert length_conversion(1, "Kilometer", "Meter") == approx(1000)
    assert length_conversion(1, "Meter", "Kilometer") == approx(0.001)
    assert length_conversion(1, "Centimeter", "Milimeter") == approx(10)
    assert length_conversion(1, "Mile", "Yard") == approx(1760)
    assert length_conversion(1, "Mile", "Meter") == approx(1609.34)
    assert length_conversion(1, "Foot", "Inch") == approx(12)
    assert length_conversion(1, "Nautical Mile", "Inch") == approx(72913.4)
    assert length_conversion(1, "Nautical Mile", "Centimeter") == approx(185200)
    assert length_conversion(50, "Foot", "Centimeter") == approx(1524)
    assert length_conversion(19, "Inch", "Mile") == approx(0.000299874)
    assert length_conversion(8000000, "Milimeter", "Kilometer") == approx(8)
    assert length_conversion(20, "Yard", "Nautical Mile") == approx(0.00987473)
    assert length_conversion(603, "Meter", "Meter") == approx(603)
    assert length_conversion("20", "Yard", "Mile") == "Value Incorrect or not found"
    assert length_conversion(20, "Yard", "") == "Value Incorrect or not found"
    assert length_conversion(2030, "yard", "nautical mile") == "Value Incorrect or not found"
    assert length_conversion(0, "", "") == "Value Incorrect or not found"
    assert length_conversion(20, "", "Meter") == "Value Incorrect or not found"



def test_mass_conversion():
    """Test if the mass_conversion function works correctly.
    Parameters: None
    Return: None
    """
    assert mass_conversion(1, "Kilogram", "Gram") == approx(1000)
    assert mass_conversion(1, "Gram", "Miligram") == approx(1000)
    assert mass_conversion(1, "Kilogram", "Miligram") == approx(100000)
    assert mass_conversion(36, "Kilogram", "Pound") == approx(79.36631)
    assert mass_conversion(101, "Kilogram", "Ton") == approx(0.101)
    assert mass_conversion(230, "Gram", "Pound") == approx(0.507063616)
    assert mass_conversion(500, "Ounce", "Pound") == approx(31.25)
    assert mass_conversion(130, "Ounce", "Gram") == approx(3685.435)
    assert mass_conversion(90, "Ton", "Pound") == approx(198415.8)
    assert mass_conversion(10, "Ton", "Gram") == approx(10000000)
    assert mass_conversion(302, "Miligram", "Ounce") == approx(0.010652745)
    assert mass_conversion(1, "Gram", "Gram") == approx(1)
    assert mass_conversion(1, "", "Gram") == "Value Incorrect or not found"
    assert mass_conversion(60, "Pound", "gram") == "Value Incorrect or not found"
    assert mass_conversion("35", "Kilogram", "Ounce") == "Value Incorrect or not found"
    assert mass_conversion("Ton", 6, "Miligram") == "Value Incorrect or not found"
    assert mass_conversion(198, "", "") == "Value Incorrect or not found"

pytest.main(["-v", "--tb=line", "-rN", __file__])
