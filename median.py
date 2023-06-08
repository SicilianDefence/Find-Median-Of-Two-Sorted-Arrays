class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        
        if length % 2 == 1:
            return merged[length // 2]
        else:
            return (merged[length // 2] + merged[length // 2 - 1]) / 2