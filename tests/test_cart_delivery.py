import pytest

from cart_delivery import qualifies_free_delivery


# Requirement 3.2.1: S$50.00 (5000 cents) or more qualifies for free delivery
@pytest.mark.parametrize("total_cents", [
    5000,   # exactly S$50.00
    5001,   # just above S$50.00
    10000,  # well above S$50.00
])
def test_total_of_5000_cents_or_more_returns_true(total_cents):
    # Arrange: input comes from the parametrize data
    # Act
    result = qualifies_free_delivery(total_cents)
    # Assert
    assert result is True


# Requirement 3.2.2: below S$50.00 does not qualify for free delivery
@pytest.mark.parametrize("total_cents", [
    0,      # lowest valid total
    1,      # just above zero
    4999,   # just below S$50.00
])
def test_total_below_5000_cents_returns_false(total_cents):
    # Arrange: input comes from the parametrize data
    # Act
    result = qualifies_free_delivery(total_cents)
    # Assert
    assert result is False


# General requirement 4: correct type but outside the permitted range
def test_negative_total_raises_value_error():
    # Arrange
    total_cents = -1
    # Act and Assert
    with pytest.raises(ValueError):
        qualifies_free_delivery(total_cents)


# General requirement 3: invalid data type
@pytest.mark.parametrize("total_cents", [
    "5000",     # string
    50.0,       # float
    None,       # missing value
])
def test_non_integer_total_raises_type_error(total_cents):
    # Arrange: input comes from the parametrize data
    # Act and Assert
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)


# General requirement 2: True and False are not valid integers
@pytest.mark.parametrize("total_cents", [True, False])
def test_boolean_total_raises_type_error(total_cents):
    # Arrange: input comes from the parametrize data
    # Act and Assert
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)
