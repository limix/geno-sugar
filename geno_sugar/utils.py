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
    bim_out = bim[Isnp]
    G_out = G[bim_out.i.values]
    pd.options.mode.chained_assignment = None
    bim_out.i = sp.arange(G_out.shape[0])
    pd.options.mode.chained_assignment = "warn"
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
    G : (`n_snps`, `n_inds`) array
        Genetic data

    Returns
    -------
    G_out : standardized array
    """
    if type(G) == da.core.Array:
        G = G.compute()
    std = G.std(1)[:, None]
    mean = G.mean(1)[:, None]
    return (G - mean) / std


def unique_variants(G, bim):
    r"""
    Filters out variants with the same genetic profile.

    Parameters
    ----------
        G : (`n_snps`, `n_inds`) array
            Genetic data
        bim : pandas.DataFrame
            Variant annotation

    Returns
    -------
        G_out : (`n_snps`, `n_inds`) array
            filtered genetic data
        bim_out : dataframe
            filtered variant annotation
    """
    if type(G) == da.core.Array:
        G = G.compute()
    _s = sp.dot(G, sp.rand(G.shape[1]))
    v, ix = sp.unique(_s, return_index=True)
    Isnp = sp.in1d(sp.arange(_s.shape[0]), ix)
    return snp_query(G, bim, Isnp)

