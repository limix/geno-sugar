from .utils import standardize_snps
import scipy as sp


def filter_by_missing(max_miss=0.01):
    """
    return function that filters by missing values
    (takes maximum fraction of missing values, default is 0.01)
    """
    def f(G, bim):
        Isnp = sp.isnan(G).mean(0) < max_miss
        G_out = G[:, Isnp]
        bim_out = bim[Isnp]
        return G_out, bim_out
    return f


def filter_by_maf(min_maf=0.01):
    """
    return function that filters by maf
    (takes minimum maf, default is 0.01)
    """
    def f(G, bim):
        maf = 0.5 * G.mean(0)
        maf[maf>0.5] = 1. - maf[maf>0.5]
        Isnp = maf > min_maf
        G_out = G[:, Isnp]
        bim_out = bim[Isnp]
        return G_out, bim_out
    return f


def standardize():
    """
    return variant standarize function
    """
    def f(G, bim):
        G_out = standardize_snps(G)
        return G_out, bim
    return f


def impute(imputer):
    """
    return impute function
    """
    def f(G, bim):
        return imputer.fit_transform(G), bim
    return f


def compose(func_list):
    """
    composion of preprocessing functions
    """
    def f(G, bim):
        for func in func_list:
            G, bim = func(G, bim)
        return G, bim
    return f
