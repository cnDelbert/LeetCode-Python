class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minus = True if dividend * divisor < 0 else False
        result = 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            count = 1
            divisorExp = divisor

            while dividend >= divisorExp:
                dividend -= divisorExp
                result += count

                count += count
                divisorExp += divisorExp

        if minus:
            if result < -2147483648:
                return -2147483648
            else:
                return -result
        else:
            if result > 2147483647:
                return 2147483647
            else:
                return result
