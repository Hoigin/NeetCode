class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        array = []
        i = 0
        while i <= (m + n) // 2:
            i += 1
            if not nums1:
                array.append(nums2.pop())
                continue
            if not nums2:
                array.append(nums1.pop())
                continue
            if nums1[-1] > nums2[-1]:
                array.append(nums1.pop())
            else:
                array.append(nums2.pop())
        print(array)
        if (m + n) % 2 == 0:
            return (array[-1] + array[-2]) / 2
        else:
            return array[-1]