from .mandelbrot import mandelbrot_par


class BaseFractal:
    def __init__(self,
                 x_range=(0., 1.),
                 y_range=(0., 1.),
                 resolution=(100, 100)):
        assert len(x_range) >= 2
        assert len(y_range) >= 2
        assert len(resolution) >= 2

        self.x_range = float(x_range[0]), float(x_range[1])
        self.y_range = float(y_range[0]), float(y_range[1])
        self.resolution = int(resolution[0]), int(resolution[1])

    def calculate(self):
        raise NotImplementedError('BaseFractal is not intended for direct use')


class Mandelbrot(BaseFractal):
    def __init__(self, x_range=(0., 1.),
                 y_range=(0., 1.),
                 resolution=(100, 100),
                 maxit=100):
        super().__init__(x_range=x_range, y_range=y_range, resolution=resolution)
        self.maxit = int(maxit)

    def calculate(self):
        return mandelbrot_par(*self.x_range,
                              *self.y_range,
                              *self.resolution,
                              self.maxit)
