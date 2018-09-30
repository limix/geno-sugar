r"""
*********
Geno Sugar
*********

Utilities perform geno-wide association analyses using bed and bgen files

"""
from __future__ import absolute_import as _
from .utils import snp_query
from .utils import is_in
from .utils import standardize_snps
from .utils import unique_variants
from .geno_queue import GenoQueue
from . import preprocess

__version__ = '0.0.1'

__all__ = ['GenoQueue', 'preprocess', 'utils', '__version__']


