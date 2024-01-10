from typing import List


        

def isValidSudoku(board: List[List[str]]) -> bool:
    i_elems = {}
    j_elems = {}
    quadrant = {}
    for i in range(9):
        i_elems[i] = []
        j_elems[i] = []
        quadrant[i] = []

    for i in range(9):
        for j in range(9):
            board_elem = board[i][j]
            if board_elem == ".":
                continue
            elems = i_elems[i]
            if board_elem in elems:
                return False
            elems.append(board_elem)

            elems = j_elems[j]
            if board_elem in elems:
                return False
            elems.append(board_elem)

            elems = quadrant[get_quadrant(i, j)]
            if board_elem in elems:
                return False
            elems.append(board_elem)

    return True


def get_quadrant(i, j):
    if 0 <= i < 3 and  0 <= j < 3:
        return 0
    if 0 <= i < 3 and  3 <= j < 6:
        return 1
    if 0 <= i < 3 and  6 <= j < 9:
        return 2
    if 3 <= i < 6 and  0 <= j < 3:
        return 3
    if 3 <= i < 6 and  3 <= j < 6:
        return 4
    if 3 <= i < 6 and  6 <= j < 9:
        return 5
    if 6 <= i < 9 and  0 <= j < 3:
        return 6
    if 6 <= i < 9 and  3 <= j < 6:
        return 7
    if 6 <= i < 9 and  6 <= j < 9:
        return 8

   
if __name__ == "__main__":

    print(isValidSudoku([
                        ["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))

    print(isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))