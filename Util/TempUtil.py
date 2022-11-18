class TempUtil:
    @staticmethod
    def celsiusToFahrenheit(celsiusTemp):
        return ((9/5) * celsiusTemp) + 32

    @staticmethod
    def fahrenheitToCelsius(fahrenheitTemp):
        return (fahrenheitTemp - 32) * (5/9)

    @staticmethod
    def transformToCelsius(fTemps):
        cTemps = []
        for fTemp in fTemps:
            cTemps.append(TempUtil.fahrenheitToCelsius(fTemp))
        return cTemps

    @staticmethod
    def transformToFahrenheit(cTemps):
        fTemps = []
        for cTemp in cTemps:
            fTemps.append(TempUtil.celsiusToFahrenheit(cTemp))
        return fTemps