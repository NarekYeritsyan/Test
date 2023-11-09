def isPowerOfTwo(n):
    if not (-2**31 <= n <= 2**31 - 1):
        return False

    return n > 0 and (n & (n - 1)) == 0

print(isPowerOfTwo(256))