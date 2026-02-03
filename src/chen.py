from AAttractor.Aattractor import AAttractor


class ChenAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 40
        c = 28
        b = 3
        dx = a * (y - x)
        dy = (c - a) * x - x * z + c * y
        dz = x * y - b * z
        return dx, dy, dz
