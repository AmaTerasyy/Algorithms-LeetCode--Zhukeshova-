class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)   # частоты
        heap = []

        for num, count in freq.items():     # кладём в кучу
            heapq.heappush(heap, (count, num))
            if len(heap) > k:               # ограничиваем размер
                heapq.heappop(heap)

        return [num for count, num in heap] # ответ