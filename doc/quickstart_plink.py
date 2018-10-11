import numpy as np
from pandas_plink import read_plink
import geno_sugar as gs
from sklearn.impute import SimpleImputer
import geno_sugar.preprocess as prep
from numpy.random import RandomState


if __name__ == "__main__":

    # define random state
    random = RandomState(1)

    # import genotype file
    bedfile = "data_structlmm/chrom22_subsample20_maf0.10"
    (bim, fam, G) = read_plink(bedfile)

    # subsample snps
    Isnp = gs.is_in(bim, ("22", 17500000, 28500000))
    G, bim = gs.snp_query(G, bim, Isnp)

    # define geno preprocessing function
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    preprocess = prep.compose([
                    prep.filter_by_missing(max_miss=0.10),
                    prep.impute(imputer),
                    prep.filter_by_maf(min_maf=0.10),
                    prep.standardize()
                    ])

    # define filtering function
    filter = gs.unique_variants

    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess)
    for _G, _bim in queue:
        # run genetic analysis
        print('Result:', np.einsum('is,is->', random.rand(*_G.shape), _G))
