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
    filter : function
        filter function
    preprocess : function
        preprocess function
    """
    def __init__(self,
                    G,
                    bim,
                    batch_size=1000,
                    preprocess=None,
                    filter=None):
        self.G = G
        self.bim = bim
        self.batch_size = batch_size
        self.preprocess = preprocess
        self.filter = filter 
        self.current = 0
        self.end = bim.shape[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            import pdb
            pdb.set_trace()
            _end = self.current + self.batch_size
            Isnp = (self.bim.i>=self.current) & (self.bim.i<_end)
            G_out, bim_out = snp_query(self.G, self.bim, Isnp)
            if self.preprocess is not None:
                G_out = self.preprocess(G_out)
            if self.filter is not None:
                G_out, bim_out = self.filter(G_out, bim_out)
            self.current = _end
            return G_out, bim_out

    def next(self):  # for python2 compatibility
        return self.__next__()
