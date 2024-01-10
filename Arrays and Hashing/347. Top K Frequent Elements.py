from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
        counter = {}
        
        for n in nums:
            n_sum = counter.get(n, 0)
            n_sum += 1
            counter[n] = n_sum
        
        
        find_max = [[] for i in range(len(nums) + 1)]

        for n, v in counter.items():
              find_max[v].append(n)

        temp_elems = []
        for i in range(len(nums), 0, -1):
            if not find_max[i]:
                  continue
            
            temp_elems += find_max[i]

            if len(temp_elems) >= k:
                  break
        return temp_elems[:k]

if __name__ == "__main__":
      print(topKFrequent([1,1,1,2,2,3], 2))
