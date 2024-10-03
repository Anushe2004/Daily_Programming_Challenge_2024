class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def lowestCommonAncestor(root,  p, q):
    # Base case: if root is None, or root is either p or q
        if not root or root == p or root == q:
            return root

    # Recursively find LCA in left and right subtrees
        left = lowestCommonAncestor(root.left, p, q) # type: ignore
        right = lowestCommonAncestor(root.right, p, q) # type: ignore

    
        if left and right:
           return root

    
        return left if left else right

CA
