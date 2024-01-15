from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water_h = 0
        i, j = 0, len(height) - 1
        out = 0

        while i < j:
            min_height = min(height[i], height[j])
            if min_height <= water_h:
                out -= min_height
            elif min_height > water_h:
                # remove water that pillar covers
                out -= water_h

                # add new layer of water (subtracting already existing layer) for the range between two pillars
                out += (j - i - 1) * (min_height - water_h)
                water_h = min_height

            if min_height == height[i]:
                i += 1
            elif min_height == height[j]:
                j -= 1
        return out


if __name__ == "__main__":
    a = Solution()
    print(a.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    print(a.trap(height = [4,2,0,3,2,5]))