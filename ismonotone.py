def is_monotone(heights):
    '''Determine if heights are monotone'''

    if heights:
        print(range(len(heights)))
        for i in range(1, len(heights)):
            if heights[i] >= heights[i-1]:
                pass
            else:
                return False

        return True

    else:
        return True


print(is_monotone([1, 2, 4]))
