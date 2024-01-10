from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # hasher = {}

    # for num in nums:
    #     hasher[num] = num
    
    # for num in nums:
    #     num_plus_1 = hasher.get(num + 1, num)
    #     hasher[num] = num_plus_1

    # nums = nums[::-1]
    # for num in nums:
    #     next_num = hasher.get(num)
    #     hasher[num] = hasher.get(next_num)
    # smallest_order = 0
    # for key, value in hasher.items():
    #     order_count = abs(key - value) + 1
    #     if order_count > smallest_order:
    #         smallest_order = order_count
    
    # return smallest_order

    num_set = set(nums)
    starting_nums = {}

    for num in num_set:
        if num - 1 in num_set:
            continue

        length = 0
        while (num + length) in num_set:
            length += 1

        starting_nums[num] = length
    
    return max(starting_nums.values())
            
if __name__ == "__main__":
    print(sorted([-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]))
    print(longestConsecutive([-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]))

    print(longestConsecutive([100,4,200,1,3,2]))
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))