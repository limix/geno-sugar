import numpy as np
from geno_sugar.utils import standardize_snps


def test_preprocess():
    random = np.random.RandomState(0)
    X = random.randn(3, 4)
    np.testing.assert_allclose(standardize_snps(X).mean(), [0, 0, 0], atol=1e-7)
    np.testing.assert_allclose(standardize_snps(X).std(), [1, 1, 1], atol=1e-7)
