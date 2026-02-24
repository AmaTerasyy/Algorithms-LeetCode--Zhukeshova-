class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       # переворачиваем камни в отрицательные, чтобы min-heap стал max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)  # превращаем список в кучу

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # самый тяжёлый
            x = -heapq.heappop(heap)  # второй по тяжести

            if y != x:
                heapq.heappush(heap, -(y - x))  # добавляем разницу обратно

        return -heap[0] if heap else 0  