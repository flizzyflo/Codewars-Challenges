"""
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) 
of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of 
its digits is divisible by 2, reverse that chunk; otherwise rotate 
it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:

revrot("123456987654", 6) --> "234561 876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561".

"""

def revrot(input_string: str, size: int) -> str:
    
    if not input_string or size <= 0 or size > len(input_string):
        return ""

    chunks = chunkify_string(input_string, size)

    return "".join([rotate(chunk) if need_to_rotate(chunk) else reverse(chunk) for chunk in chunks])
               

def chunkify_string(input_string: str, size: int, chunked_strings: list[str] = []) -> list[str]:

    """Splits the string put in as argument into several chunks of size 'size'. 
    If last chunk is smaller than size, its not chunked anymore and the chunked strings are returned."""

    if len(input_string) < size:
        return chunked_strings
    
    else:
        chunked_strings.append(input_string[:size])
        return chunkify_string(input_string[size:], size, chunked_strings)


def cubify_digits(input_string: str) -> int:

    """Returns the sum of the cubified single digits of an numerical string put in as argument."""

    return sum(int(number) ** 3 for number in input_string)


def need_to_rotate(input_string: str) -> bool:

    """Checks if a strings needs to be rotated."""

    if cubify_digits(input_string) % 2 == 0:
        return False
    
    return True


def rotate(input_string: str) -> str:

    """Rotates the string to the left. Most left character becomes the most right one."""

    return input_string[1:len(input_string)] + input_string[0]


def reverse(input_string: str) -> str:
    return "".join(letter for letter in input_string[::-1])
