
# ['Ac', 'Ks', '5h', 'Td', '3c'] -> [0, 2 ,22, 30, 51] //encoding
# [0, 51, 30, 22, 2] -> ['Ac', '3c', 'Td', '5h', 'Ks'] //decoding
#    c     |     d     |    h     |    s
# ----------------------------------------
#  0: A      13: A      26: A      39: A
#  1: 2      14: 2      27: 2      40: 2
#  2: 3      15: 3      28: 3      41: 3
#  3: 4      16: 4      29: 4      42: 4
#  4: 5      17: 5      30: 5      43: 5
#  5: 6      18: 6      31: 6      44: 6
#  6: 7      19: 7      32: 7      45: 7
#  7: 8      20: 8      33: 8      46: 8
#  8: 9      21: 9      34: 9      47: 9
#  9: T      22: T      35: T      48: T
# 10: J      23: J      36: J      49: J
# 11: Q      24: Q      37: Q      50: Q
# 12: K      25: K      38: K      51: K

def generate_card_values(base_dict: dict[str, int]) -> dict[str, int]:
    return {str(key): value + 13 for key, value in base_dict.items()}

def generate_total_values():
    c = {str(key): value for key, value in enumerate(range(1, 9), 2)}
    c["A"] = 0
    c["T"] = 9
    c["J"] = 10
    c["Q"] = 11
    c["K"] = 12

    d = generate_card_values(c)
    h = generate_card_values(d)
    s = generate_card_values(h)

    return {"c": c, "d": d, "h": h, "s": s}


def evaluate_type(cur_type: str) -> bool:
    overall = generate_total_values()
    d = {"c": 1, "d": 2, "h": 3, "s": 4}
    multiplier = d[cur_type[1]]
    return multiplier * overall[cur_type[1]][cur_type[0]]


def encode(cards: list[str]) -> list[int]:
    card_values = generate_total_values()
    return sorted([card_values[card[1]][card[0]] for card in cards])


def decode(cards: list[str]) -> list[str]:
    card_values = generate_total_values()

    return sorted([key+type for type in card_values.keys() for key, value in card_values[type].items() if value in cards], reverse= False, key= lambda a:  evaluate_type(a))

t= encode(['Ac', 'Ks', '5h', 'Td', '3c'])
print(t)
print(decode([0, 51, 30, 22, 2]))
