# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("x")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        n = len(data)
        def dfs(i):
            if i == n or data[i] == "x":
                return None, i
            node = TreeNode(int(data[i]))
            node.left, i = dfs(i+1)
            node.right, i = dfs(i+1)
            return node, i
        res, _ = dfs(0)
        return res
