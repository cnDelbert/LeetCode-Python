class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = 0
        r_s = []
        vowel_rev_list = [l for l in s if l.lower() in "aeiou"][::-1]
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                r_s.append(vowel_rev_list[j])
                j += 1
            else:
                r_s.append(s[i])
        return "".join(r_s)