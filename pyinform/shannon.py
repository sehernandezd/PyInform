# Copyright 2016 ELIFE. All rights reserved.
# Use of this source code is governed by a MIT
# license that can be found in the LICENSE file.
import numpy as np

from ctypes import c_double, c_void_p
from pyinform import _inform
from pyinform.dist import Dist

def entropy(dist, b=2.0):
    """
    Compute the base-`b` shannon entropy of a distribution `dist`.
    """
    return _entropy(dist._dist, c_double(b))

_entropy = _inform.inform_shannon
_entropy.argtypes = [c_void_p, c_double]
_entropy.restype = c_double