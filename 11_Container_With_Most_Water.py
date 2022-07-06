## 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max = 0
        left = 0
        right = len(height)-1
        while (left < right):
            area = min(height[left], height[right]) * (right-left)
            if area > max:
                max = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max
S = Solution()
y = S.maxArea([1,8,6,2,5,4,8,3,7])
print(y)
