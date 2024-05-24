# 7. Python Exception Handling
# 1. Exceptional Weather Forecast

def get_fahrenheit_temperature():
    while True:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            return fahrenheit
        except ValueError:
            print("Please enter a valid numerical value for the temperature.")

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except ZeroDivisionError:
        print("Error: Division by zero occurred during temperature conversion.")
        return None

def main():
    try:
        temperature_fahrenheit = get_fahrenheit_temperature()
        celsius_temperature = fahrenheit_to_celsius(temperature_fahrenheit)
        if celsius_temperature is not None:
            print(f"Converted temperature: {celsius_temperature:.2f}°C")
    except KeyboardInterrupt:
        print("\nUser interrupted the program.")
    finally:
        print("Thank you for using the weather forecast application!")

if __name__ == "__main__":
    main()
