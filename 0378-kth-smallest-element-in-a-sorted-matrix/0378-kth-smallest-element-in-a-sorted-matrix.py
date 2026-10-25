class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n=len(matrix); lo,hi=matrix[0][0],matrix[n-1][n-1]
        while lo<hi:
            mid=(lo+hi)//2; cnt=0; j=n-1
            for i in range(n):
                while j>=0 and matrix[i][j]>mid: j-=1
                cnt+=j+1
            if cnt<k: 
                lo=mid+1
            else: 
                hi=mid
        return lo