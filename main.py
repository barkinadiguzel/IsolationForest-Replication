from src.core.iforest import iForest
from src.core.path_length import path_length
from src.math.score import anomaly_score

X = [[1,2], [2,1], [3,5], [10,10], [12,11]]  # 2 anomalys which are 10,10 and 12,11
forest = iForest(n_trees=50, subsample_size=4)
forest.fit(X)

for x in X:
    paths = [path_length(x, t) for t in forest.trees]
    s = anomaly_score(sum(paths)/len(paths), len(X))
    print(f"Point {x}, anomaly score: {s:.2f}")
