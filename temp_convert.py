#temp convert : takes input as a temp1 and coverts it into format format2 . Just takes simple mathematical statements and makes use of match case statement


def celsiustofahrenheit(celsius):
    return (celsius * 9/5) + 32



def celsiustokelvin(celsius):
    return celsius + 273.15



def fahrenheittocelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9



def fahrenheittokelvin(fahrenheit):
    celsius = fahrenheittocelsius(fahrenheit)
    return celsiustokelvin(celsius)



def kelvintocelsius(kelvin):
    return kelvin - 273.15



def kelvintofahrenheit(kelvin):
    celsius = kelvintocelsius(kelvin)
    return celsiustofahrenheit(celsius)


while True:
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")
    
    choice = input("Enter: (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        temperature = float(input("Enter temperature value: "))
        if choice == '1':
            result = celsiustofahrenheit(temperature)
            print(f"{temperature}°C is equal to {result}°F")
        elif choice == '2':
            result = celsiustokelvin(temperature)
            print(f"{temperature}°C is equal to {result} K")
        elif choice == '3':
            result = fahrenheittocelsius(temperature)
            print(f"{temperature}°F is equal to {result}°C")
        elif choice == '4':
            result = fahrenheittokelvin(temperature)
            print(f"{temperature}°F is equal to {result} K")
        elif choice == '5':
            result = kelvintocelsius(temperature)
            print(f"{temperature} K is equal to {result}°C")
        elif choice == '6':
            result = kelvintofahrenheit(temperature)
            print(f"{temperature} K is equal to {result}°F")
    else:
        print("Invalid Input")