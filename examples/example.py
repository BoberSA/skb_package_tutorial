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