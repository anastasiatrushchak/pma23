def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n