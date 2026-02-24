def ft_count_harvest_recursive() -> None:
    """Count down the days until harvest recursively
    """
    days = int(input("Days until harvest: "))
    count_days(1, days)


def count_days(current: int, total: int) -> None:
    """count the day before harvest time

    Args:
        current (int): current day number
        total (int): total number of days until harvest
    """
    if current > total:
        print("Harvest time!")
        return
    print(f"Day {current}")
    count_days(current + 1, total)
