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

def test_transformToCelsius():
    fTemps = [32, 5, -13, 86]
    result = TempUtil.transformToCelsius(fTemps)
    assert len(fTemps) == len(result)
    assert result[0] == 0
    assert result[1] == -15
    assert result[2] == -25
    assert result[3] == 30

def test_transformToFahrenheit():
    cTemps = [0, -32, 32, 86]
    result = TempUtil.transformToFahrenheit(cTemps)
    assert len(cTemps) == len(result)
    assert result[0] == 32
    assert result[1] == -25.6
    assert result[2] == 89.6
