class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        freq_gap = {}
        for i in range(0,n):
            freq_gap[nums[i]]=0
        j = 0
        for k in freq_gap:
            nums[j] = k
            j += 1
        return j