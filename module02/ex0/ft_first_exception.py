#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    temperature = 0
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return -1
    except Exception:
        print("Error: something went wrong")
        return -1

    if temperature < 0:
        print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        return -1
    elif temperature > 40:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        return -1
    else:
        print(f"Temperature {temperature}°C is perfect for plants!")
        return temperature


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    _ = check_temperature("25")

    print("\nTesting temperature: abc")
    _ = check_temperature("abc")

    print("\nTesting temperature: 100")
    _ = check_temperature("100")

    print("\nTesting temperature: -50")
    _ = check_temperature("-50")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
