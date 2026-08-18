class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            ans = target - nums[i]
            for j in range(n):
                if i != j and nums[j] == ans:
                    return [i,j]