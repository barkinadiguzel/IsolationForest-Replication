import random

def subsample(X, psi):
    return random.sample(X, min(psi, len(X)))
