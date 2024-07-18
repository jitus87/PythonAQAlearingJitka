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

def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Example usage:
n = 100# Change this value to find a different nth prime number
sheldons_prime = find_nth_prime(n)
print(f"Sheldon's {n}th prime number is: {sheldons_prime}")