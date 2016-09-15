class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            while n:
                if n % 3 and n != 1:
                    return False
                else:
                    n /= 3
            return True
        return False
