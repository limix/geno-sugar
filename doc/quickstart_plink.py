import numpy as np
from pandas_plink import read_plink
import geno_sugar as gs
from sklearn.preprocessing import Imputer


if __name__ == "__main__":

    # import genotype file
    bedfile = "data_structlmm/chrom22_subsample20_maf0.10"
    (bim, fam, G) = read_plink(bedfile)

    # subsample snps
    Isnp = gs.is_in(bim, ("22", 17500000, 18500000))
    G, bim = gs.snp_query(G, bim, Isnp)

    # define geno preprocessing function
    impute = gs.preprocess.impute(
        Imputer(missing_values=np.nan, strategy="mean", axis=1)
    )
    standardize = gs.preprocess.standardize()
    preprocess = gs.preprocess.compose([impute, standardize])

    # define filtering function
    filter = gs.unique_variants

    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess, filter=filter)
    for _G, _bim in queue:
        print(".. loaded %d/%d variants" % (_G.shape[0], G.shape[0]))
