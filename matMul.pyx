import cython
import numpy as np
cimport numpy as np


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef multiply(A, B):
    return A*B

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef divide(A, B):
    return A/B

