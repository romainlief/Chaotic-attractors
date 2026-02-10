from Attractor.AAttractor.Aattractor import AAttractor


class HalvorsenAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 1.89
        dx = -a * x - 4 * y - 4 * z - y * y
        dy = -a * y - 4 * z - 4 * x - z * z
        dz = -a * z - 4 * x - 4 * y - x * x
        return dx, dy, dz
