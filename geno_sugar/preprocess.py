import scipy as sp
from .composition import compose_funcs
from .utils import standardize_snps


def standardize():
    """
    return variant standarize function
    """
    return standardize_snps


def impute(imputer):
    """
    return fit transform function of sklearn imputer
    """
    return imputer.fit_transform


def compose(func_list):
    """
    creates a composion of preprocessing functions
    """
    return compose_funcs(func_list)
