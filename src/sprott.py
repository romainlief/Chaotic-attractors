from Aattractor import AAttractor


class SprottAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 2.07
        b = 1.79
        dx = y + a * x * y + x * z
        dy = 1 - b * x * x + y * z
        dz = x - x * x - y * y
        return dx, dy, dz
