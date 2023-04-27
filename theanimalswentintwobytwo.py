
def two_by_two(animals: list[str]) -> dict[str, int]:

    if not animals:
        return False

    return {animal: 2 for animal in animals if animals.count(animal) >= 2}

