def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    A prime num is greater than 1 and has no divisors other than 1 and itself.
    Parameters:
        n (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
