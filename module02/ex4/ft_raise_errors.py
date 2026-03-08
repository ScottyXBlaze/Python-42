def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty")
    if 1 > water_level:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
        )
    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )
    if 2 > sunlight_hours:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    return f"Plant {plant_name} is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===", end="\n\n")
    print("Testing good values...")
    print(check_plant_health("tomato", 7, 10))

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 10, 9))
    except Exception as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("apple", 15, 4))
    except Exception as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("apple", 1, 0))
    except Exception as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
