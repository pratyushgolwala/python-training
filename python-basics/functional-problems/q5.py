#Q5
import math
def wind_chill(t, v):
    if t > 50 or v < 3:
        return "not defined for these values."
    else:
        w = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(math.pow(v, 0.16))
        return f"wind chill is: {w}"
    
    
temperature = int(input("Enter temperature in Fahrenheit: "))
wind_speed = int(input("Enter wind speed in miles per hour: "))
print(wind_chill(temperature, wind_speed))