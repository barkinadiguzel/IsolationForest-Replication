import random
from ..utils.split import random_split

class iTreeNode:
    def __init__(self, left=None, right=None, split_attr=None, split_value=None, size=None):
        self.left = left
        self.right = right
        self.split_attr = split_attr
        self.split_value = split_value
        self.size = size  

def iTree(X, current_height=0, height_limit=float('inf')):
    if current_height >= height_limit or len(X) <= 1:
        return iTreeNode(size=len(X))  
    q, p = random_split(X)  
    X_left = [x for x in X if x[q] < p]
    X_right = [x for x in X if x[q] >= p]
    left = iTree(X_left, current_height + 1, height_limit)
    right = iTree(X_right, current_height + 1, height_limit)
    return iTreeNode(left, right, q, p)
