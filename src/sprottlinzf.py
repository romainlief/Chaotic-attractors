from AAttractor.Aattractor import AAttractor


class SprottLinzFAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 0.5
        dx = y + z
        dy = - x + a * y
        dz = x * x - z
        return dx, dy, dz
