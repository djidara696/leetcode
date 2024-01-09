from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    # greatest_right = []

    # for i in range(len(arr)):
    #     if i == len(arr) - 1:
    #         greatest_right.append(-1)
    #         break

    #     greatest_right.append(max(arr[i + 1:]))

    # return greatest_right

    rightMax = -1
    for i in range(len(arr) -1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
    return arr

    

print(replaceElements([17,18,5,4,6,1]))