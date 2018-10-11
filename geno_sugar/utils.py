import scipy as sp
import pandas as pd
import dask.array as da


def snp_query(G, bim, Isnp):
    r"""
    Parameters
    ----------
    G : (`n_snps`, `n_inds`) array
        Genetic data
    bim : pandas.DataFrame
        Variant annotation
    Isnp : bool array
        Variant filter

    Returns
    -------
    G_out : (`n_snps`, `n_inds`) array
        filtered genetic data
    bim_out : dataframe
        filtered variant annotation
    """
    bim_out = bim[Isnp].reset_index(drop=True)
    G_out = G[bim_out.i.values]
    bim_out.i = pd.Series(sp.arange(bim_out.shape[0]), index=bim_out.index)
    return G_out, bim_out


def is_in(bim, geno_range):
    r"""
    Parameters
    ----------
    bim : pandas.DataFrame
        Variant annotation
    geno_range : tuple
        (chrom, pos_start, pos_end)

    Returns
    -------
    Isnp : bool array
        Variant filter
    """
    Ichrom = bim.chrom == geno_range[0]
    Ipos1 = bim.pos >= geno_range[1]
    Ipos2 = bim.pos < geno_range[2]
    return Ichrom & Ipos1 & Ipos2


def standardize_snps(G):
    r"""
    Standardize variantes.

    Parameters
    ----------
    G : (`n_inds`, `n_snps`) array
        Genetic data

    Returns
    -------
    G_out : standardized array
    """
    mean = G.mean(0)
    std = G.std(0)
    return (G - mean) / std


def unique_variants(G):
    r"""
    Filters out variants with the same genetic profile.

    Parameters
    ----------
        G : (`n_inds`, `n_snps`) array
            Genetic data

    Returns
    -------
        G_out : (`n_inds`, `n_unique_snps`) array
            filtered genetic data
        idxs : int array
            indexes of the the unique variants
    """
    _s = sp.dot(sp.rand(G.shape[0]), G)
    v, ix = sp.unique(_s, return_index=True)
    ix = sp.sort(ix)
    G_out = G[:, ix]
    return G_out, Isnp
