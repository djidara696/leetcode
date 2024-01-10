from typing import List


def generateParenthesis(n: int) -> List[str]:

    def open_parantheses(current_paranthesie: str, open_p: int, closed_p: int, n: int, all_elements: List[str]) -> str:
        open_p += 1
        if open_p < n:
            open_parantheses(current_paranthesie + "(", open_p, closed_p, n, all_elements)
        
        if open_p > closed_p and closed_p < n:
            close_parantheses(current_paranthesie + ")", open_p, closed_p, n, all_elements)
        
        if open_p == n and closed_p == n:
            all_elements.append(current_paranthesie)

    def close_parantheses(current_paranthesie: str, open_p: int, closed_p: int, n: int, all_elements: List[str]) -> List[str]:
        closed_p += 1
        if open_p < n:
            open_parantheses(current_paranthesie + "(", open_p, closed_p, n, all_elements)
        
        if open_p > closed_p and closed_p < n:
            close_parantheses(current_paranthesie + ")", open_p, closed_p, n, all_elements)
        
        if open_p == n and closed_p == n:
            all_elements.append(current_paranthesie)

    all_elements = []
    open_p   = 0
    closed_p = 0

    open_parantheses("(", open_p, closed_p, n, all_elements)
    return all_elements

    



if __name__ == "__main__":       
    print(generateParenthesis(4))