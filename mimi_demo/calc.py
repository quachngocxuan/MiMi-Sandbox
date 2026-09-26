def add(a: float, b: float) -> float:
    return a + b


def average(values: list[float]) -> float:
    if not values:
        raise ValueError("average of an empty list")
    return sum(values) / len(values)
