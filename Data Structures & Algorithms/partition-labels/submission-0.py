class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = dict()
        res = []
        for i, l in enumerate(s):
            pos[l] = i
        size = 0
        end = 0
        for i, l in enumerate(s):
            size += 1
            end = max(end, pos[l])
            if i == end:
                res.append(size)
                size = 0
        return res