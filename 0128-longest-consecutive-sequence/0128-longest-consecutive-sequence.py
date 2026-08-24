class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        dic = set(nums)
        for num in dic:
            if num - 1 not in dic:
                current = num
                count = 1
                while current + 1 in dic:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest

            