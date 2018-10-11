r"""
*********
Geno Sugar
*********

Utilities perform geno-wide association analyses using bed and bgen files

"""
from __future__ import absolute_import as _absolute_import
from .utils import snp_query
from .utils import is_in
from .utils import standardize_snps
from .utils import unique_variants
from ._sh import download
from ._sh import unzip
from .geno_queue import GenoQueue
from . import preprocess
from ._testit import test

__version__ = "0.0.1"

__all__ = [
    "GenoQueue",
    "standardize_snps",
    "preprocess",
    "utils",
    "snp_query",
    "is_in",
    "unique_variants",
    "download",
    "unzip",
    "test",
    "__version__",
]
