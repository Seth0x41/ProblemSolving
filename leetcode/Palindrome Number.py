class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and int(str(x)[::-1]) - x == 0:
            return True
        else:
            return False