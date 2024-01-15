from typing import List
import itertools

# Too slow, too many conversions

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = set()
#         for combination in itertools.combinations(nums, 3):

#             if sum(combination) != 0:
#                 continue

#             results.add(tuple(list(sorted(list(combination)))))

#         return [list(x) for x in results]



# Too slow and complex

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         passed_elements = set()
#         i, j, k = 0, 1, 2
#         while i < len(nums) - 2:
#             while j < len(nums) - 1:
                
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     sorted_entity = sorted([nums[i], nums[j], nums[k]])

#                     if sorted_entity not in results:
#                         results.append(sorted_entity)
#                         passed_elements |= set([(nums[i], nums[j]), (nums[j], nums[i]), 
#                                                 (nums[i], nums[k]), (nums[k], nums[i]),
#                                                 (nums[j], nums[k]), (nums[k], nums[j])])

#                     j += 1
#                     k = j + 1
#                     if k == len(nums):
#                         j += 1
#                         k = j + 1
#                     continue
#                 k += 1

#                 if k == len(nums) or (nums[i], nums[j]) in passed_elements:
#                     j += 1
#                     k = j + 1

#             i += 1
#             j = i + 1
#             k = j + 1
#             while (nums[i], nums[j]) in passed_elements:
#                 i += 1
#                 j = i + 1
#                 k = j + 1
#                 if i >= len(nums) - 2:
#                     break

#         return results

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        solution = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break

            if i > 0 and v == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                res = v + nums[j] + nums[k]

                if res > 0:
                    k -= 1
                elif res < 0:
                    j += 1
                else:
                    solution.append([v,  nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return solution

                


if __name__ == "__main__":
    a = Solution()
    print(a.threeSum([-1,0,1,2,-1,-4]))
    print(a.threeSum([0,1,1]))
    print(a.threeSum([0,0,0]))
