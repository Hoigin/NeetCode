import heapq

class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []
        self.minlen, self.maxlen = 0, 0

    def addNum(self, num: int) -> None:
        if self.minlen >= self.maxlen:
            heapq.heappush(self.maxheap, -num)
            self.maxlen += 1
        else:
            heapq.heappush(self.minheap, num)
            self.minlen += 1
        if len(self.minheap) == 0:
            return
        if -self.maxheap[0] > self.minheap[0]:
            tmp1 = -heapq.heappop(self.maxheap)
            tmp2 = heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, tmp1)
            heapq.heappush(self.maxheap, -tmp2)  

    def findMedian(self) -> float:
        if (self.maxlen + self.minlen) % 2 == 1:
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2        