from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groupper = {}

    for s in strs:
        
        sorted_str = "".join(sorted(list(s)))

        elements = groupper.get(sorted_str, [])
        elements.append(s)
        groupper[sorted_str] = elements

    return list(groupper.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["t"]))