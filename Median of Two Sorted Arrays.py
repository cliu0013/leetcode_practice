class Solution(object):
    def res(self, i, j, A, B, m, n):  
        if i == 0: max_of_left = B[j-1]
        elif j == 0: max_of_left = A[i-1]
        else: max_of_left = max(A[i-1], B[j-1])

        if (m + n) % 2 == 1:
            return max_of_left

        if i == m: min_of_right = B[j]
        elif j == n: min_of_right = A[i]
        else: min_of_right = min(A[i], B[j])

        return (max_of_left + min_of_right) / 2.0

        
    def recur(self, imin, imax, A, B, m, n):
        i = (imin + imax)/2
        j = (m + n + 1)/2 - i
        if imin == imax:
            return self.res(i, j, A, B, m, n)
        if (j > 0 and B[j - 1] > A[i]):
            imin = i + 1
            return self.recur(imin, imax, A, B, m, n)
        elif (i > 0 and A[i - 1] > B[j]):
            imax = i - 1 
            return self.recur(imin, imax, A, B, m, n)
        else:
            return self.res(i, j, A, B, m, n)
        
        
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin = 0
        imax = m
        return self.recur(imin, imax, nums1, nums2, m, n)
        