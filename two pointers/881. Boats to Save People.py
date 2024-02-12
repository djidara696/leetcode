from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while people:

            if i == j:
                boats += len(people)
                break
            
            first_p  = people[i]
            second_p = people[j]

            if first_p + second_p <= limit:
                boats += 1
                people.pop(i)
                people.pop(j - 1)
                j = j - 2 if j - 2 >= 0 else 0

            else:
                j -= 1
        
        return boats







if __name__ == "__main__":
    a = Solution()

    print(a.numRescueBoats(people = [3,1,7], limit = 7))
    print(a.numRescueBoats(people = [5,1,4,2], limit = 6))
    print(a.numRescueBoats(people = [3,2,2,1], limit = 3))
    print(a.numRescueBoats(people = [3,5,3,4], limit = 5))