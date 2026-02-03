from AAttractor.Aattractor import AAttractor


class SprottBAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 0.4
        b = 1.2
        c = 1
        dx = a * y * z
        dy = x - b * y
        dz = c - x * y
        return dx, dy, dz
