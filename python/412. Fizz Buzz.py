class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def cal_num(value):
            if value % 3 == 0:
                if value %5 == 0:
                    return 'FizzBuzz'
                else:
                    return 'Fizz'
            if value % 5 == 0:
                return 'Buzz'
            return str(value)
        return [cal_num(value) for value in range(1, n+1)]
