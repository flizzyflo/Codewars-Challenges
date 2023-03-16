#https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr: str, k: int):
    i = 0
    word_list = list()

    if (k > len(strarr)) or (k < 0):
        return ""

    while k <= len(strarr):
        word_list.append("".join(strarr[i:k]))
        i += 1
        k += 1

    return max(word_list, key=len)

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))

