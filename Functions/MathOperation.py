
def is_pair(cislo):
    if cislo & 1:
        return False
    else:
        return True


def is_prime(num):
    """Check if a number is a prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_middle_char(string):
    length = len(string)
    if not is_pair(length):
        middle_index = length // 2
        middle_index2 = middle_index
    else:
        middle_index = (length // 2) - 1
        middle_index2 = length // 2
    return middle_index, middle_index2