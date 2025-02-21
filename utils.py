import re

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_temperature():
    while True:
        temp_input = input("Enter temperature (e.g., 37°C or 98.6°F): ").strip()
        
        match = re.match(r"^(\d+(\.\d+)?)\s?([CFcf]?)$", temp_input)
        if match:
            temp_value = match.group(1)
            unit = match.group(3).upper() if match.group(3) else "C"
            return f"{temp_value}°{unit}"
        else:
            print("Invalid format. Please enter a valid temperature (e.g., 37°C or 98.6°F).")
