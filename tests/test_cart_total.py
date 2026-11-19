import pytest

from cart_total import calculate_total


# Requirement 3.1.1: total = unit price x quantity
@pytest.mark.parametrize("unit_price_cents, quantity, expected_total", [
    (250, 1, 250),
    (250, 4, 1000),
    (1999, 3, 5997),
])
def test_valid_price_and_quantity_returns_price_times_quantity(unit_price_cents, quantity, expected_total):
    # Arrange: inputs come from the parametrize data
    # Act
    result = calculate_total(unit_price_cents, quantity)
    # Assert
    assert result == expected_total


# Requirement 3.1.2: a unit price or quantity of zero gives a total of zero
@pytest.mark.parametrize("unit_price_cents, quantity", [
    (0, 5),     # zero unit price
    (250, 0),   # zero quantity
    (0, 0),     # both zero
])
def test_zero_price_or_quantity_returns_zero(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize data
    # Act
    result = calculate_total(unit_price_cents, quantity)
    # Assert
    assert result == 0


# Requirement 3.1.3: the total is returned in cents as an integer
def test_valid_price_and_quantity_returns_int():
    # Arrange
    unit_price_cents = 250
    quantity = 4
    # Act
    result = calculate_total(unit_price_cents, quantity)
    # Assert
    assert type(result) is int


# General requirement 4: correct type but outside the permitted range
@pytest.mark.parametrize("unit_price_cents, quantity", [
    (-1, 3),    # negative unit price
    (250, -1),  # negative quantity
    (-1, -1),   # both negative
])
def test_negative_price_or_quantity_raises_value_error(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize data
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_total(unit_price_cents, quantity)


# General requirement 3: invalid data type
@pytest.mark.parametrize("unit_price_cents, quantity", [
    ("250", 3),     # string price
    (2.5, 3),       # float price
    (None, 3),      # missing price
    (250, "3"),     # string quantity
    (250, 3.0),     # float quantity
    (250, None),    # missing quantity
])
def test_non_integer_price_or_quantity_raises_type_error(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize data
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_total(unit_price_cents, quantity)


# General requirement 2: True and False are not valid integers
@pytest.mark.parametrize("unit_price_cents, quantity", [
    (True, 3),      # boolean price
    (250, False),   # boolean quantity
])
def test_boolean_price_or_quantity_raises_type_error(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize data
    # Act and Assert
    with pytest.raises(TypeError):
        calculate_total(unit_price_cents, quantity)
