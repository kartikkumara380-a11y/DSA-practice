class Solution:
    def secondHighest(self, s: str) -> int:
        digit = ""
        for ch in s:
            if ch.isdigit():
                digit += ch
        largest = -1
        s_largest = -1
        for i in range(len(digit)):
            largest = max(largest,int(digit[i]))
        for i in range(len(digit)):
            if int(digit[i]) > s_largest and int(digit[i]) != largest:
                s_largest = int(digit[i])
        return s_largest
        if not s_largest:
            return -1

