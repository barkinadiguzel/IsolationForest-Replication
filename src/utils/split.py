import random

def random_split(X):
    if len(X) == 0:
        return 0, 0
    n_features = len(X[0])
    q = random.randint(0, n_features - 1)
    feature_values = [x[q] for x in X]
    p = random.uniform(min(feature_values), max(feature_values))
    return q, p
