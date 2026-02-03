from math import sin, pi
from Aattractor import AAttractor


class ChuaAttractor(AAttractor):
    def __init__(self, alpha=10.82, beta=14.286) -> None:
        super().__init__()
        self.alpha = alpha
        self.beta = beta

    def derivatives(self, state):
        x, y, z = state
        a = 1.3
        c = 7
        b = 0.11
        d = 0
        h = -b * sin((pi * x / 2 * a) + d)
        dx = self.alpha * (y - h)
        dy = x - y + z
        dz = -self.beta * y
        return dx, dy, dz
