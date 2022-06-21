class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squerdlist=[num**2 for num in nums]
        squerdlist.sort()
        return squerdlist
