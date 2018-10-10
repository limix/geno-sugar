import numpy as np
from geno_sugar.preprocess import standardize


def test_preprocess():
    random = np.random.RandomState(0)
    X = random.randn(3, 4)
    np.testing.assert_allclose(standardize()(X).mean(axis=1), [0, 0, 0], atol=1e-7)
    np.testing.assert_allclose(standardize()(X).std(axis=1), [1, 1, 1], atol=1e-7)
