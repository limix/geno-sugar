.. _quickstart:

*********************
Quick Start in Python
*********************

We here show how to run geno-wide analysis using plink and bgen files
using geno-sugar.


Plink file example
^^^^^^^^^^^^^^^^^^

We need to first download and extract BED files, and then proceed with the example
of reading them.

.. testcleanup::

    import os
    import shutil

    if os.path.exists("data_structlmm.zip"):
        os.remove("data_structlmm.zip")

    if os.path.exists("data_structlmm"):
        shutil.rmtree("data_structlmm")

.. testcode::

    import numpy as np
    from pandas_plink import read_plink
    from sklearn.impute import SimpleImputer
    
    import geno_sugar as gs
    import geno_sugar.preprocess as prep

    
    gs.download("http://www.ebi.ac.uk/~casale/data_structlmm.zip")
    gs.unzip("data_structlmm.zip")
    
    # define random state
    random = np.random.RandomState(1)
    
    # import genotype file
    bedfile = "data_structlmm/chrom22_subsample20_maf0.10"
    (bim, fam, G) = read_plink(bedfile, verbose=False)
    
    # subsample snps
    Isnp = gs.is_in(bim, ("22", 17500000, 28500000))
    G, bim = gs.snp_query(G, bim, Isnp)
    
    # define geno preprocessing function
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    preprocess = prep.compose(
        [
            prep.filter_by_missing(max_miss=0.10),
            prep.impute(imputer),
            prep.filter_by_maf(min_maf=0.10),
            prep.standardize(),
        ]
    )
    
    # define filtering function
    filter = gs.unique_variants
    
    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess)
    for _G, _bim in queue:
        # run genetic analysis
        print("Result:", np.einsum("is,is->", random.rand(*_G.shape), _G))

.. testoutput::

    .. read 200 / 15929 variants (1.26%)
    Result: 39.31615841973354
    .. read 400 / 15929 variants (2.51%)
    Result: 60.14859050496203
    .. read 600 / 15929 variants (3.77%)
    Result: 55.331152201803974
    .. read 800 / 15929 variants (5.02%)
    Result: -6.754660482524052
    .. read 1000 / 15929 variants (6.28%)
    Result: -53.0330138600346
    .. read 1200 / 15929 variants (7.53%)
    Result: -28.67740460227282
    .. read 1400 / 15929 variants (8.79%)
    Result: -52.79766992650515
    .. read 1600 / 15929 variants (10.04%)
    Result: 79.23948191402047
    .. read 1800 / 15929 variants (11.30%)
    Result: -31.970194355365024
    .. read 2000 / 15929 variants (12.56%)
    Result: 24.525441851113786
    .. read 2200 / 15929 variants (13.81%)
    Result: -48.154400096220584
    .. read 2400 / 15929 variants (15.07%)
    Result: -62.707711729788215
    .. read 2600 / 15929 variants (16.32%)
    Result: 136.40189146745564
    .. read 2800 / 15929 variants (17.58%)
    Result: 98.58366080355582
    .. read 3000 / 15929 variants (18.83%)
    Result: -17.91015348468791
    .. read 3200 / 15929 variants (20.09%)
    Result: 36.21731334424119
    .. read 3400 / 15929 variants (21.34%)
    Result: 76.66526289877936
    .. read 3600 / 15929 variants (22.60%)
    Result: 2.2764654983047485
    .. read 3800 / 15929 variants (23.86%)
    Result: 72.3204050130708
    .. read 4000 / 15929 variants (25.11%)
    Result: 41.708157458158894
    .. read 4200 / 15929 variants (26.37%)
    Result: 4.48703122701581
    .. read 4400 / 15929 variants (27.62%)
    Result: -75.69136000949241
    .. read 4600 / 15929 variants (28.88%)
    Result: 48.13702616216051
    .. read 4800 / 15929 variants (30.13%)
    Result: 40.69527425370762
    .. read 5000 / 15929 variants (31.39%)
    Result: 41.55059257637385
    .. read 5200 / 15929 variants (32.64%)
    Result: 29.746125051086196
    .. read 5400 / 15929 variants (33.90%)
    Result: -146.22678609888834
    .. read 5600 / 15929 variants (35.16%)
    Result: 85.3328467745588
    .. read 5800 / 15929 variants (36.41%)
    Result: 60.41791541164633
    .. read 6000 / 15929 variants (37.67%)
    Result: -124.87024172520883
    .. read 6200 / 15929 variants (38.92%)
    Result: -36.578181837560756
    .. read 6400 / 15929 variants (40.18%)
    Result: -38.469877156502115
    .. read 6600 / 15929 variants (41.43%)
    Result: -138.4592756656873
    .. read 6800 / 15929 variants (42.69%)
    Result: 56.577704329353125
    .. read 7000 / 15929 variants (43.95%)
    Result: -80.6127449445221
    .. read 7200 / 15929 variants (45.20%)
    Result: -11.449427386001588
    .. read 7400 / 15929 variants (46.46%)
    Result: -93.54900003659337
    .. read 7600 / 15929 variants (47.71%)
    Result: -6.744703955747619
    .. read 7800 / 15929 variants (48.97%)
    Result: -44.129987933106094
    .. read 8000 / 15929 variants (50.22%)
    Result: -32.74345970500676
    .. read 8200 / 15929 variants (51.48%)
    Result: -64.23327234685601
    .. read 8400 / 15929 variants (52.73%)
    Result: 108.2817141901817
    .. read 8600 / 15929 variants (53.99%)
    Result: -41.89605216445146
    .. read 8800 / 15929 variants (55.25%)
    Result: -155.60904006432918
    .. read 9000 / 15929 variants (56.50%)
    Result: -42.593669143248114
    .. read 9200 / 15929 variants (57.76%)
    Result: 70.25528000060257
    .. read 9400 / 15929 variants (59.01%)
    Result: 3.0340936971777346
    .. read 9600 / 15929 variants (60.27%)
    Result: 89.61512757137238
    .. read 9800 / 15929 variants (61.52%)
    Result: 72.34002346267535
    .. read 10000 / 15929 variants (62.78%)
    Result: 117.11832615272706
    .. read 10200 / 15929 variants (64.03%)
    Result: -14.743982350445938
    .. read 10400 / 15929 variants (65.29%)
    Result: 11.98705299203688
    .. read 10600 / 15929 variants (66.55%)
    Result: 111.43049301844309
    .. read 10800 / 15929 variants (67.80%)
    Result: -14.315709132899778
    .. read 11000 / 15929 variants (69.06%)
    Result: 48.617625544156496
    .. read 11200 / 15929 variants (70.31%)
    Result: -20.00727644211451
    .. read 11400 / 15929 variants (71.57%)
    Result: -59.300078720370834
    .. read 11600 / 15929 variants (72.82%)
    Result: 46.00359413870454
    .. read 11800 / 15929 variants (74.08%)
    Result: 72.30226579174433
    .. read 12000 / 15929 variants (75.33%)
    Result: -61.685905978762975
    .. read 12200 / 15929 variants (76.59%)
    Result: 29.078820766788667
    .. read 12400 / 15929 variants (77.85%)
    Result: -42.94694959575352
    .. read 12600 / 15929 variants (79.10%)
    Result: -71.69481829181149
    .. read 12800 / 15929 variants (80.36%)
    Result: -19.13047845855384
    .. read 13000 / 15929 variants (81.61%)
    Result: -78.25805157473718
    .. read 13200 / 15929 variants (82.87%)
    Result: -134.4075742710578
    .. read 13400 / 15929 variants (84.12%)
    Result: 106.09895668041852
    .. read 13600 / 15929 variants (85.38%)
    Result: -127.45465981769064
    .. read 13800 / 15929 variants (86.63%)
    Result: -18.335427508625894
    .. read 14000 / 15929 variants (87.89%)
    Result: 98.20454314478086
    .. read 14200 / 15929 variants (89.15%)
    Result: 18.86291543490482
    .. read 14400 / 15929 variants (90.40%)
    Result: 83.5512500268531
    .. read 14600 / 15929 variants (91.66%)
    Result: 67.78377400714238
    .. read 14800 / 15929 variants (92.91%)
    Result: -12.928835500603215
    .. read 15000 / 15929 variants (94.17%)
    Result: -64.7657284402363
    .. read 15200 / 15929 variants (95.42%)
    Result: -29.27809775283688
    .. read 15400 / 15929 variants (96.68%)
    Result: -25.711359348095776
    .. read 15600 / 15929 variants (97.93%)
    Result: 36.17358874299279
    .. read 15800 / 15929 variants (99.19%)
    Result: -106.72796041500679
    .. read 15929 / 15929 variants (100.00%)
    Result: -87.96227721980513


Bgen file example
^^^^^^^^^^^^^^^^^

.. testcleanup::

    import os

    if os.path.exists("example.bgen"):
        os.remove("example.bgen")

.. testcode::

    import numpy as np
    from numpy.random import RandomState
    from bgen_reader import read_bgen, compute_dosage, allele_expectation
    from sklearn.impute import SimpleImputer

    import geno_sugar as gs
    import geno_sugar.preprocess as prep

    gs.download(
        "https://github.com/limix/bgen-reader-py/blob/master/example/example.bgen?raw=true"
    )

    # define random state
    random = RandomState(1)

    # import genotype file
    bgen_file = "example.bgen"
    bgen = read_bgen(bgen_file, verbose=False)
    bim = bgen["variants"]
    bim["i"] = range(len(bim))
    G = compute_dosage(allele_expectation(bgen["genotype"], nalleles=2, ploidy=2))
    print(bim)
    print(G)

    # subsample snps
    Isnp = gs.is_in(bim, ("01", 10000, 14000))
    G, bim = gs.snp_query(G, bim, Isnp)

    # define geno preprocessing function
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    preprocess = prep.compose(
        [
            prep.filter_by_missing(max_miss=0.10),
            prep.impute(imputer),
            prep.filter_by_maf(min_maf=0.10),
            prep.standardize(),
        ]
    )

    # define filtering function
    filter = gs.unique_variants

    # loop on geno
    queue = gs.GenoQueue(G, bim, batch_size=200, preprocess=preprocess)
    for _G, _bim in queue:
        # run genetic analysis
        print("Result:", np.einsum("is,is->", random.rand(*_G.shape), _G))

.. testoutput::

                id      rsid chrom     pos  nalleles allele_ids    i
    0      SNPID_2    RSID_2    01    2000         2        A,G    0
    1      SNPID_3    RSID_3    01    3000         2        A,G    1
    2      SNPID_4    RSID_4    01    4000         2        A,G    2
    3      SNPID_5    RSID_5    01    5000         2        A,G    3
    4      SNPID_6    RSID_6    01    6000         2        A,G    4
    5      SNPID_7    RSID_7    01    7000         2        A,G    5
    6      SNPID_8    RSID_8    01    8000         2        A,G    6
    7      SNPID_9    RSID_9    01    9000         2        A,G    7
    8     SNPID_10   RSID_10    01   10000         2        A,G    8
    9     SNPID_11   RSID_11    01   11000         2        A,G    9
    10    SNPID_12   RSID_12    01   12000         2        A,G   10
    11    SNPID_13   RSID_13    01   13000         2        A,G   11
    12    SNPID_14   RSID_14    01   14000         2        A,G   12
    13    SNPID_15   RSID_15    01   15000         2        A,G   13
    14    SNPID_16   RSID_16    01   16000         2        A,G   14
    15    SNPID_17   RSID_17    01   17000         2        A,G   15
    16    SNPID_18   RSID_18    01   18000         2        A,G   16
    17    SNPID_19   RSID_19    01   19000         2        A,G   17
    18    SNPID_20   RSID_20    01   20000         2        A,G   18
    19    SNPID_21   RSID_21    01   21000         2        A,G   19
    20    SNPID_22   RSID_22    01   22000         2        A,G   20
    21    SNPID_23   RSID_23    01   23000         2        A,G   21
    22    SNPID_24   RSID_24    01   24000         2        A,G   22
    23    SNPID_25   RSID_25    01   25000         2        A,G   23
    24    SNPID_26   RSID_26    01   26000         2        A,G   24
    25    SNPID_27   RSID_27    01   27000         2        A,G   25
    26    SNPID_28   RSID_28    01   28000         2        A,G   26
    27    SNPID_29   RSID_29    01   29000         2        A,G   27
    28    SNPID_30   RSID_30    01   30000         2        A,G   28
    29    SNPID_31   RSID_31    01   31000         2        A,G   29
    ..         ...       ...   ...     ...       ...        ...  ...
    169  SNPID_171  RSID_171    01   71001         2        A,G  169
    170  SNPID_172  RSID_172    01   72001         2        A,G  170
    171  SNPID_173  RSID_173    01   73001         2        A,G  171
    172  SNPID_174  RSID_174    01   74001         2        A,G  172
    173  SNPID_175  RSID_175    01   75001         2        A,G  173
    174  SNPID_176  RSID_176    01   76001         2        A,G  174
    175  SNPID_177  RSID_177    01   77001         2        A,G  175
    176  SNPID_178  RSID_178    01   78001         2        A,G  176
    177  SNPID_179  RSID_179    01   79001         2        A,G  177
    178  SNPID_180  RSID_180    01   80001         2        A,G  178
    179  SNPID_181  RSID_181    01   81001         2        A,G  179
    180  SNPID_182  RSID_182    01   82001         2        A,G  180
    181  SNPID_183  RSID_183    01   83001         2        A,G  181
    182  SNPID_184  RSID_184    01   84001         2        A,G  182
    183  SNPID_185  RSID_185    01   85001         2        A,G  183
    184  SNPID_186  RSID_186    01   86001         2        A,G  184
    185  SNPID_187  RSID_187    01   87001         2        A,G  185
    186  SNPID_188  RSID_188    01   88001         2        A,G  186
    187  SNPID_189  RSID_189    01   89001         2        A,G  187
    188  SNPID_190  RSID_190    01   90001         2        A,G  188
    189  SNPID_191  RSID_191    01   91001         2        A,G  189
    190  SNPID_192  RSID_192    01   92001         2        A,G  190
    191  SNPID_193  RSID_193    01   93001         2        A,G  191
    192  SNPID_194  RSID_194    01   94001         2        A,G  192
    193  SNPID_195  RSID_195    01   95001         2        A,G  193
    194  SNPID_196  RSID_196    01   96001         2        A,G  194
    195  SNPID_197  RSID_197    01   97001         2        A,G  195
    196  SNPID_198  RSID_198    01   98001         2        A,G  196
    197  SNPID_199  RSID_199    01   99001         2        A,G  197
    198  SNPID_200  RSID_200    01  100001         2        A,G  198
    <BLANKLINE>
    [199 rows x 7 columns]
    dask.array<getitem, shape=(199, 500), dtype=float64, chunksize=(199, 500)>
    .. read 9 / 9 variants (100.00%)
    Result: -13.85549311486657