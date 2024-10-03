FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
temp = float(input("Enter the temperature to convert: "))
    
def convert_to_fahrenheit(celsius):
    if unit == "c":
        celsius = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{temp}°F is {celsius}°C")


def convert_to_celsius(fahrenheit):
    if unit == "f":
        fahrenheit = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print (f"{temp}°C is {fahrenheit}°F")
if __name__ == "__main__":
    convert_to_fahrenheit(celsius=temp)
    convert_to_celsius(fahrenheit=temp)
