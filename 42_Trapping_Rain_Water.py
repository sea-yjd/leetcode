# 42. Trapping Rain Water
class Solution:
    def trap(self, height: list[int]) -> int:
        """
        # 超时
        :param height:
        :return:
        area = 0
        for i in range(len(height)):
            left = 0
            for j in range(i):
                if j >= 0:
                    left = max(left, height[j])
            right = 0
            for j in range(i+1, len(height)):
                right = max(right, height[j])
            area += max(0, min(left, right) - height[i])
        return area
        """
        area = 0
        left_max = 0
        right_max = 0
        i = 0
        j = len(height)-1
        while(i < j):
            if height[i] <= height[j]:
                if height[i] > left_max:
                    left_max = height[i]
                else:
                    area += left_max - height[i]
                i += 1
            else:
                if height[j] > right_max:
                    right_max = height[j]
                else:
                    area += right_max - height[j]
                j -= 1
        return area
S = Solution()
y = S.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(y)
