
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