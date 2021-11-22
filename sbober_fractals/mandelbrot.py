import numpy as np
from numba import njit, prange


@njit(fastmath=True, cache=True)
def escape(x0, y0, maxit=1000):
    x, y = 0, 0
    i = 0
    for i in range(maxit):
        x, y = x*x - y*y + x0, 2*x*y + y0
        if x*x + y*y > 4:
            break
    return i

@njit(parallel=True, fastmath=True, cache=True)
def mandelbrot_par(xmin, xmax, ymin, ymax, nx, ny, maxit=1000):
    dx = (xmax - xmin) / nx
    dy = (ymax - ymin) / ny
    arr = np.empty((ny, nx), dtype=np.uint16)
    for iy in prange(ny):
        for ix in range(nx):
            x = xmin + dx * ix
            y = ymin + dy * iy
            it = escape(x, y, maxit)
            arr[iy, ix] = it
    return arr