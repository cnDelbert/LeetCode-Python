class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x).startswith('+') or str(x).startswith('-'):
            return 0 if int(str(x)[0] + str(x)[-1:0:-1]) < -2147483647-1 else int(str(x)[0] + str(x)[-1:0:-1])
        return 0 if int(str(x)[::-1]) > 2147483647 else int(str(x)[::-1])