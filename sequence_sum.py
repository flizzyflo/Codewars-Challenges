
def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    
    """Arithmetic sequence formula to calculate the sum of sequence"""

    if (begin_number > end_number and step > 0):
        return 0

    if (begin_number < end_number and step < 0):
        return 0

    # calculate number of single elements within the sequence
    terms = ((end_number - begin_number) // step) + 1

    return (terms * (2 * begin_number + (terms - 1) * step)) // 2 

