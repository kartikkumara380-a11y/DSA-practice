class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            
        sorted_items = sorted(freq.items(), key = lambda item: item[1], reverse = True)
        ans = ""
        for ch, count in sorted_items:
            ans += ch * count
        return ans