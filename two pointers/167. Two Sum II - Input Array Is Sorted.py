


from typing import List

# Too slow
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]
                
#                 if numbers[i] + numbers[j] > target:
#                     break


class Solution:
    

    def get_index(self, next_number: int, current_i: int, hashed_values: dict) -> int:
        indexes = hashed_values.get(next_number)
        for j in indexes:
            if j > current_i:
                return j
            
        return None
        

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashed_values = {}
        for i, v in enumerate(numbers):

            indexes = hashed_values.get(v, [])
            indexes.append(i)
            hashed_values[v] = indexes

        for i in range(len(numbers)):
            next_num = target - numbers[i]
            
            if hashed_values.get(next_num):
                second_i = self.get_index(next_num, i, hashed_values)
                if not second_i: continue

                return [i + 1, second_i + 1]


a = Solution()

print(a.twoSum(numbers = [2,7,11,15], target = 9))
print(a.twoSum(numbers = [2,3,4], target = 6))
print(a.twoSum(numbers = [-1,0], target = -1))
