

def approx_two(n: int, liste= [1, 1]) -> float:
    """Diese Funktion erzeugt eine Folge von Brüchen, die sich immer mehr der Wurzel von 2 annähern.
    Sie gibt das n-te Wertpaar aus, welches die Wurzel 2 approximiert."""

    for i in range(1, n):
        helper = liste[0]
        liste[0] = liste[0] + liste[1]
        liste[1] = liste[0] + helper
    return liste[1]/liste[0]

