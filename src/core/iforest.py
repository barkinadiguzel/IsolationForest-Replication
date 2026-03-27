from .itree import iTree
from ..utils.sampling import subsample

class iForest:
    def __init__(self, n_trees=100, subsample_size=256):
        self.n_trees = n_trees
        self.subsample_size = subsample_size
        self.trees = []

    def fit(self, X):
        self.trees = []
        for _ in range(self.n_trees):
            X_sub = subsample(X, self.subsample_size)
            height_limit = int(self.subsample_size).bit_length()  
            tree = iTree(X_sub, 0, height_limit)
            self.trees.append(tree)
