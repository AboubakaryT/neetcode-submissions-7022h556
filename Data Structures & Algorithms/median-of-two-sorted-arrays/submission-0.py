class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total= len(nums1) + len(nums2)
        half = (len(nums1) + len(nums2)) // 2
        
        #We know that we will find a median no matter what
        if(len(nums1) >= len(nums2)):
                nums1, nums2 = nums2, nums1
        l = 0 
        r = len(nums1) 
        
        while l <= r:
            partitionX = (l+r) // 2
            partitionY = (total + 1) // 2 - partitionX
            #reduce out of bound exceptions
            l1 = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            r1 = float ('inf') if partitionX == len(nums1) else nums1[partitionX]
            l2 = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            r2 = float('inf') if partitionY == len(nums2) else nums2[partitionY]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1,r2)) / 2
                else:
                    return max(l1,l2)
            else:
                #binary search
                if l1 > r2:
                    r = partitionX - 1
                else:
                    l = partitionX + 1


