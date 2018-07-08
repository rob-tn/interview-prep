"""
    Median of two sorted arrays of size m and n respectively
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # find medians of both arrays, then get sum of medians
        # works for non-duplicate arrays

        if len(nums1) == 0:
            med1 = None
        elif len(nums1) == 1:
            med1 = nums1[0]
        elif len(nums1) % 2 == 0:
            med1 = (nums1[len(nums1)/2 - 1] + nums1[len(nums1)/2]) / 2.0
        else:
            med1 = nums1[len(nums1)/2]

        if len(nums2) == 0:
            med2 = None
        elif len(nums2) == 1:
            med2 = nums2[0]
        elif len(nums2) % 2 == 0:
            med2 = (nums2[len(nums2)/2 - 1] + nums2[len(nums2)/2]) / 2.0
        else:
            med2 = nums2[len(nums2)/2]

        if med1 == None and med2 != None:
            return med2
        elif med1 != None and med2 == None:
            return med1
        return (med1 + med2) / 2.0

obj1 = Solution()
arr1 = [1, 2]
arr2 = [3, 4]

arr3 = [1, 2, 3, 4]
arr4 = [7, 8, 9, 10]

arr5 = [5, 6, 10, 15, 16, 17, 18, 20, 25, 30]
arr6 = [1,4, 7, 8, 13]

print(obj1.findMedianSortedArrays(arr1, arr2))
print(obj1.findMedianSortedArrays(arr3, arr4))
print(obj1.findMedianSortedArrays(arr5, arr6))