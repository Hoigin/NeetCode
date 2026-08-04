class MedianFinder:

    def __init__(self):
        self.lower, self.upper = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.upper, -heapq.heappushpop(self.lower, -num))
        if len(self.lower) < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return (self.upper[0] - self.lower[0]) / 2 
        