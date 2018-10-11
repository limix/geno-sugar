from .utils import snp_query


class GenoQueue:
    """
    Util class for genome wide analysis

    Parameters
    ----------
    G : (snps, inds) array
        Genetic data
    bim : pandas.DataFrame
        Variant annotation
    batch_size : int
        number of snps in the batch
    preprocess : function
        preprocess function
    verbose : bool
        verbose flag (default True)
    """

    def __init__(self, G, bim, batch_size=1000, preprocess=None, verbose=True):
        self.G = G
        self.bim = bim
        self.batch_size = batch_size
        self.preprocess = preprocess
        self.visited_snps = 0
        self.current = 0
        self.end = bim.shape[0]
        self.verbose = verbose

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            _end = self.current + self.batch_size
            Isnp = (self.bim.i >= self.current) & (self.bim.i < _end)
            G_out, bim_out = snp_query(self.G, self.bim, Isnp)
            self.visited_snps += G_out.shape[0]
            G_out = G_out.compute().T
            if self.preprocess is not None:
                G_out, bim_out = self.preprocess(G_out, bim_out)
            self.current = _end
            if self.verbose:
                fraction = 100. * self.visited_snps / float(self.G.shape[0])
                msg = '.. read %d / %d variants (%.2f%%)'
                msg %= (self.visited_snps,  self.G.shape[0], fraction)
                print(msg)
            return G_out, bim_out

    def next(self):  # for python2 compatibility
        return self.__next__()
