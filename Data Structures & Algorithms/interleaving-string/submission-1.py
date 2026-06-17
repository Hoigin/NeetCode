class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 如果长度之和不相等，绝对不可能交错组成
        if len(s1) + len(s2) != len(s3):
            return False
            
        memo = {}
        
        def dfs(i, j):
            # 如果两个字符串都匹配完了，说明 s3 也成功匹配完了
            if i == len(s1) and j == len(s2):
                return True
            
            # 如果当前状态已经计算过，直接返回缓存结果
            if (i, j) in memo:
                return memo[(i, j)]
                
            # s3 当前需要匹配的字符索引
            k = i + j
            
            # 尝试匹配 s1 的当前字符
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    memo[(i, j)] = True
                    return True
                    
            # 尝试匹配 s2 的当前字符
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    memo[(i, j)] = True
                    return True
            
            # 两种路径都走不通，记录失败
            memo[(i, j)] = False
            return False
            
        return dfs(0, 0)