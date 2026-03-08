def water_plants(plant_list: dict[str, bool]) -> None:
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant_list[plant]:
                print(f"Watering {plant}")
            else:
                raise ValueError(
                    f"Error: cannot water {plant} - invalid plant!"
                )
        print("Watering completed successfully!")

    except ValueError as e:
        print(e)

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plants = {
        "Tomato": True,
        "lettuce": True,
        "carrots": True
    }

    print("=== Garden Watering System ===", end="\n\n")
    water_plants(plants)


if __name__ == "__main__":
    plants = {
        "Tomato": True,
        "lettuce": True,
        "carrots": True
    }
    print("=== Garden Watering System ===", end="\n\n")
    print("Testing normal watering...")

    water_plants(plants)

    print()
    plants = {
        "Tomato": True,
        None: False,
        "carrots": True
    }
    print("Testing with error...")

    water_plants(plants)

    print("\nCleanup always happens, even with errors!")
