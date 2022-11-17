from Util.TempUtil import TempUtil

def test_celsiusToFahrenheit_Freezing():
    result = TempUtil.celsiusToFahrenheit(0)
    assert result == 32

def test_celsiusToFahrenheit_BelowFreezing():
    result = TempUtil.celsiusToFahrenheit(-32)
    assert result == -25.6

def test_celsiusToFahrenheit_AboveFreezing():
    result = TempUtil.celsiusToFahrenheit(32)
    assert result == 89.6


def test_fahrenheitToCelsius_Freezing():
    result = TempUtil.fahrenheitToCelsius(32)
    assert result == 0

def test_fahrenheitToCelsius_BelowFreezing():
    result = TempUtil.fahrenheitToCelsius(5)
    assert result == -15

def test_fahrenheitToCelsius_BelowFreezing_Negative():
    result = TempUtil.fahrenheitToCelsius(-13)
    assert result == -25

def test_fahrenheitToCelsius_AboveFreezing():
    result = TempUtil.fahrenheitToCelsius(86)
    assert result == 30