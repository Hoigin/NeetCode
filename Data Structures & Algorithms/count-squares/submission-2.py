from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.dic = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.dic[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        res = 0
        
        # 遍历数据结构中所有已存在的点，将其作为正方形的“对角顶点”
        for (x, y), count in self.dic.items():
            # 构成正方形对角线的条件：
            # 1. 不能是查询点本身 (x != px 且 y != py)
            # 2. 横向距离必须等于纵向距离 (abs(px - x) == abs(py - y))
            if x == px or y == py or abs(px - x) != abs(py - y):
                continue
            
            # 根据查询点 (px, py) 和对角顶点 (x, y)，推导出另外两个顶点的坐标：
            # 顶点 1: (x, py) -> 与对角点同 X，与查询点同 Y
            # 顶点 2: (px, y) -> 与查询点同 X，与对角点同 Y
            if (x, py) in self.dic and (px, y) in self.dic:
                # 组合原理：各点可能重复添加，方案数为三种顶点数量的乘积
                res += count * self.dic[(x, py)] * self.dic[(px, y)]
                
        return res