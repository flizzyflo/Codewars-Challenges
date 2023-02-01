

def approx_two(n: int, helper=0, list= [1, 1]) -> float:
    """Diese Funktion erzeugt eine Folge von Brüchen, die sich immer mehr der Wurzel von 2 annähern.
    Sie gibt das n-te Wertpaar aus, welches die Wurzel 2 approximiert."""

    for i in range(1, n):
        helper = list[0]
        list[0] = list[0] + list[1]
        list[1] = list[0] + helper
    return list[1]/list[0]

print(approx_two(15))
