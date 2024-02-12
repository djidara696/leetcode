from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        min_n = 5000

        while l <= h:
            m = l + (h - l)//2
            if nums[l] < nums[h]:
                min_n = min(min_n, nums[l])
                break

            min_n = nums[m] if nums[m] < min_n else min_n

            
            if nums[m] >= nums[l]:
                l = m + 1 
            else:
                h = m - 1

        return min_n

            



if __name__ == "__main__":
    a = Solution()
    print(a.findMin(nums = [5,1,2,3,4]))
    print(a.findMin(nums = [3,4,5,1,2]))
    print(a.findMin(nums = [4,5,6,7,0,1,2]))
    print(a.findMin(nums = [11,13,15,17]))