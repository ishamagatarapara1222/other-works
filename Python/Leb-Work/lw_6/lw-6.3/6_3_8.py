class HighTemperatureError(Exception):
    pass

def convert_temperature(temp_input):
    # 1. Raise a TypeError if input is not a number
    if not isinstance(temp_input, (int, float)):
        raise TypeError("Temperature must be a numerical value!")
    
    # 2. Assert temperature is within absolute physical limits
    assert -273 <= temp_input <= 10000, "Temperature out of realistic physical limits (-273°C to 10,000°C)!"
    
    # 3. Raise custom exception if it exceeds 1000°C
    if temp_input > 1000:
        raise HighTemperatureError("Unrealistic temperature for common everyday applications!")
        
    # Example conversion (Celsius to Fahrenheit)
    fahrenheit = (temp_input * 9/5) + 32
    print(f"{temp_input}°C is equal to {fahrenheit}°F")

# Testing different scenarios
try:
    # Change this value to test different exceptions (e.g., "hot", 5000, 1500)
    convert_temperature(1200) 
except (TypeError, AssertionError, HighTemperatureError) as error:
    print("Error caught:", error)