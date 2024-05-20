from typing import List

class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        lo, hi = 0, n - 1
        ans = arr[0]
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if abs(k - arr[mid]) == abs(k - ans):
                ans = max(ans, arr[mid])
            elif abs(k - arr[mid]) < abs(k - ans):
                ans = arr[mid]
            
