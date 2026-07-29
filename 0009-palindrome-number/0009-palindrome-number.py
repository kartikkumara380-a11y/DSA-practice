class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        temp = x
        while x>0:
            digit = x % 10
            res = res * 10 + digit
            x = x // 10
        if temp == res:
            return True
        else:
            return False