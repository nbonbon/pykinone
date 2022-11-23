from strenum import StrEnum

class TemperatureUnit(StrEnum):
    Celsius = 'c'
    Fahrenheit = 'f'

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None