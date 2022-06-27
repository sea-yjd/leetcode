class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        l = len(nums3)
        nums3_sort = sorted(nums3)
        if l % 2 == 0:   # 偶数
            med_index1, med_index2 = int(l/2-1), int(l/2)
            med = float((nums3_sort[med_index1] + nums3_sort[med_index2]) / 2)
            return med
        else:
            return (nums3_sort[int((l-1)/2)])
