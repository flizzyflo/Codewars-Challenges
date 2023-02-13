def tower_builder(n_floors, l=[]):
    for i in range(n_floors):
        l.append(" " * (n_floors - 1 - i) + "*" * (2 * i + 1) + " " * (n_floors - 1 - i))
    return l
print(tower_builder(5))