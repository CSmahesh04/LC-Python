# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val   # gets the value of the current node
#         self.left = left # goes to the next node on the left
#         self.right = right # goes to the next node on the right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

    	if not root:	#This if will be used to return back up from the  bottom of the tree
    		return 0

    	return (max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1)

# Ok, so we start at the root, if its not null, we apply the maxDepth function on the left and right child of the root. If they are not null,
#  they call maxDepth on their left and right child nodes. This keeps going until someones child does not exist, thus returning zero for maxDepth
# then we take the max, which might be 0 or 1, then that max gets added with the 1 and it keeps going up till we back at the root node again.