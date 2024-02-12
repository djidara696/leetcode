from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1

        if matrix[-1][-1] < target  or target < matrix[0][0]:
            return False
        
        search_list = []
        while l <= h:
            m = l + (h - l)//2

            if matrix[m][0] <= target <= matrix[m][-1]:
                search_list = matrix[m]
                break

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                h = m - 1
        
        if not search_list:
            return False

        l, h = 0, len(search_list)

        while l <= h:
            n = l + (h - l)//2

            if search_list[n] == target:
                return True
            
            if target < search_list[n]:
                h = n - 1
            
            elif target > search_list[n]:
                l = n + 1
        
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(a.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 31))
    print(a.searchMatrix(matrix =  [[1],[3],[5]], target = 2))