degree = input("Entering the temp in (Celcius/Farenhite):")
temp = int(input("Enter the temp:"))
if degree.lower() == "celcius" or degree.lower() == "c":
    result = (temp * (9/5)) + 32
    print(f"Conversion to farenhiet is{result}")
elif degree.lower() == "farenhite" or degree.lower() == "f":
    result1 = (temp - 32)* (5/9)
    print(f"Conversion to celcius is{result1}")
