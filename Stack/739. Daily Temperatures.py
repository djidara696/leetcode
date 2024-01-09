

from typing import List


def dailyTemperatures( temperatures: List[int]) -> List[int]:
    # temp_indexes = {}
    # for el in set(temperatures):
    #     temp_indexes[el] = len(temperatures)
    
    # temp_ocurences = set()

    # result = []
    # for i, temp in enumerate(temperatures[::-1]):
    #     r_i = len(temperatures) - 1 - i

    #     f_temp_indexes = []
    #     for ftemp in temp_ocurences:
    #         if temp >= ftemp:
    #             continue
    #         f_temp_indexes.append(temp_indexes[ftemp] - r_i)

    #     else:
    #         if not f_temp_indexes:
    #             result.insert(0, 0)
    #         else:
    #             result.insert(0, min(f_temp_indexes))
        
    #     temp_ocurences.add(temp)
    #     temp_indexes[temp] = r_i
    result = [0] * len(temperatures)
    stack = []

    i = 0
    for i, temp in enumerate(temperatures):

        while stack and temp > stack[-1][0]:
            s_temp, s_i = stack.pop()
            result[s_i] = i - s_i

        stack.append((temp, i))


    
        



    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))