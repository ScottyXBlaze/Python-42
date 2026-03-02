def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    count_days(1, days)


def count_days(current: int, total: int) -> None:
    if current > total:
        print("Harvest time!")
        return
    print(f"Day {current}")
    count_days(current + 1, total)
