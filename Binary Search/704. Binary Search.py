from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            m = l + (h - l)//2
            
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1

        return -1

            


if __name__ == "__main__":
    a = Solution()
    print(a.search(nums = [-1,0,3,5,9,12], target = 9))
    print(a.search(nums = [-1,0,3,5,9,12], target = 2))