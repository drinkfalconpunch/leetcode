# With recursion

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        if sum >= 10:
            return self.addDigits(sum)
        return sum