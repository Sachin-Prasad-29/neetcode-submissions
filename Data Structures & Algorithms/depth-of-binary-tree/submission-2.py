# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        counter = 0
        while queue:
            tempresult = []
            tempqueue = deque()
            while queue:
                tempqueue.append(queue.popleft())
            while tempqueue:
                node = tempqueue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tempresult.append(node)
            counter += 1
        return counter