class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return "{0:0b}".format(int(a,2) + int(b, 2))
