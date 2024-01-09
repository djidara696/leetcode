from ast import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max = 0
        for i, h in enumerate(heights):
            if not st or st[-1][1] >= h:
                st.append((i, h))
            
            else:
                while st[-1][1] > h:
                    i, h 



Solution().largestRectangleArea([2,1,5,6,2,3])
