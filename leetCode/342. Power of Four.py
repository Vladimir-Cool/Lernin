

# class Solution:

def isPowerOfFour(n: int) -> bool:
    if not (n):
        return False
    if(n == 1):
        return True
    if n % 4 == 0:
        return isPowerOfFour(n/4)
    else:
        return False

print(isPowerOfFour(1))