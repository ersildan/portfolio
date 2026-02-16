class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        #
        # nums1[:] = sorted(
        #     [
        #         el
        #         for index, el in enumerate(nums1, start=1)
        #         if index <= m
        #     ]
        #     +
        #     [
        #         el
        #         for index, el in enumerate(nums2, start=1)
        #         if index <= n
        #     ]
        # )
