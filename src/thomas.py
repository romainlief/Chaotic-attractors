import numpy as np
from Aattractor import AAttractor


class ThomasAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        b = 0.208186
        dx = np.sin(y) - b * x
        dy = np.sin(z) - b * y
        dz = np.sin(x) - b * z
        return dx, dy, dz
