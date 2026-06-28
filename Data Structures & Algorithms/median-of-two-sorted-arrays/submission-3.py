class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1)

        while l <=r:
            partition1 = (l + r) // 2
            partition2 = (total + 1) // 2 - partition1
            """
            Reduce the edges cases, this is allowed, because we know
            that there will ALWAYS be a median.
            """
            l1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            r1 = float('inf') if partition1 == len(nums1) else nums1[partition1]
            l2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            r2 = float('inf') if partition2 == len(nums2) else nums2[partition2]
            
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1,r2)) / 2
                else:
                    return max(l1,l2) 
            else:
                if l1 > r2:
                    r = partition1 -1 
                else:
                    l = partition1 + 1