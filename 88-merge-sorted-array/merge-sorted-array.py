class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        for final_pointer in range(len(nums1) -1, -1, -1):
            if nums1_pointer >= 0 and nums2_pointer >= 0:
                if nums1[nums1_pointer] > nums2[nums2_pointer]:
                    nums1[final_pointer] = nums1[nums1_pointer]
                    nums1_pointer -= 1
                else:
                    nums1[final_pointer] = nums2[nums2_pointer]
                    nums2_pointer -= 1
            elif nums1_pointer >= 0:
                nums1[final_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[final_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1

        