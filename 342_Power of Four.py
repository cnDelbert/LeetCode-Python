class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return int("{num:b}".format(num=num).rstrip('0')) == 1 and len("{num:b}".format(num=num))%2 == 1 if num else False