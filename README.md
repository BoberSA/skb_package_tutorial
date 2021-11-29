# sbober_fractal

## Python Package Creation Tutorial

- classes for fractal sets calculation
- jit-compiled using Numba for fast parallel computing

## Installation

    pip install -i https://test.pypi.org/simple/ sbober-fractals

## Usage example

Requires additional `matplotlib` package.

```python
import numpy as np
import matplotlib.pyplot as plt
from sbober_fractals import Mandelbrot

fr = Mandelbrot(x_range=(-2., 2.),
                y_range=(-2., 2.),
                resolution=(400, 400),
                maxit=500)

img = fr.calculate()

plt.figure(figsize=(10,10))
plt.pcolormesh(np.linspace(*fr.x_range, fr.resolution[0]),
               np.linspace(*fr.y_range, fr.resolution[1]),
               np.log(img + 1), shading='auto',
               cmap='twilight')
plt.axis('equal')
plt.show()
```

## Developers

Stanislav Bober, [HSE Profile](https://hse.ru/staff/botas)