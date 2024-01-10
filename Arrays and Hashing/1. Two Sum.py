from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    diff_hash = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in diff_hash:
            return [i, diff_hash.get(diff)]
        
        diff_hash[n] = i
        

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))