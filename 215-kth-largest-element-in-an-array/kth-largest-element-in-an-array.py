class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Создаем min-heap из первых k элементов: O(k)
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Проходим по оставшимся элементам: O((n-k) * log k)
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
                
        # Корень кучи - k-й самый большой элемент
        return min_heap[0]