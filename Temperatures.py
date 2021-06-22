def main():
    HourlyTemperature = []
    get_temperature(HourlyTemperature)
    ave,mn,mx = avemnmx(HourlyTemperature)
    displayTemperature(HourlyTemperature)

def get_temperature(HourlyTemperature):
    for i in range(24):
        x = int(input())
        HourlyTemperature.append(x)
        return HourlyTemperature

def avemnmx(HourlyArray):
    ave = (sum())

