from enum import IntEnum

class Mode(IntEnum):
    Off = 0
    Heat = 1
    Cool = 2
    Auto = 3
    EmergencyHeat = 4

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member
        return None