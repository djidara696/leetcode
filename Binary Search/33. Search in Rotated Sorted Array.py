from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            m = l + (h - l) // 2

            if nums[m] == target:
                return m
            
            # m not in break area
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            
            # m in beak area
            else: 
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        
        return -1
            

if __name__ == "__main__":
    a = Solution()
    print(a.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(a.search(nums = [4,5,6,7,0,1,2], target = 3))
    print(a.search(nums = [5,6,7,0,1,2,4], target = 6))
    print(a.search(nums = [6,7,0,1,2,4,5], target = 0))
    print(a.search(nums = [1], target = 0))