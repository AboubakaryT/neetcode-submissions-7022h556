class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr = sorted(self.arr)

    def findMedian(self) -> float:
        m = len(self.arr) // 2
        print(self.arr)
        if len(self.arr) >= 2 and len(self.arr) % 2 == 0:
            print(self.arr[m])
            return ((self.arr[m-1]) + (self.arr[m])) / 2
        
        return self.arr[m]
        