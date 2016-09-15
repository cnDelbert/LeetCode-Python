class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_list = s.split()
        s_revert = s_list[::-1]
        return ' '.join(s_revert)
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
"""
