import itertools

def choose_best_sum(max_distance: int, max_visited_towns: int, distances: list[int]) -> int:
    
    if max_visited_towns > len(distances):
        return None

    possible_routes = create_all_possible_permutations(distances= distances, max_visited_towns= max_visited_towns, max_distance= max_distance)

    if not possible_routes:
        return None
    
    return max(sum(perm) for perm in possible_routes if sum(perm) <= max_distance)
    

def create_all_possible_permutations(max_distance: int, max_visited_towns: int, distances: list[int]) -> list[tuple[int]]:
    return list(itertools.dropwhile(lambda *x: sum(*x) > max_distance, list(itertools.combinations(distances, max_visited_towns))))

