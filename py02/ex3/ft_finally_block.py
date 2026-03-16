#!/usr/bin/env python3


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully!")
    except TypeError:
        print(f"Error: cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


test_watering_system()
