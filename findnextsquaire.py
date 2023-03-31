import math
def find_next_square(sq):
    if sq%math.sqrt(sq)==0:
        return (math.sqrt(sq)+1)**2
    else:
        return -1

print(find_next_square(114))