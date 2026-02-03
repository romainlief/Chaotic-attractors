from AAttractor.Aattractor import AAttractor


class ThreeScrollAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 32.48
        c = 1.18
        b = 45.84
        d = 0.13
        e = 0.57
        f = 14.7
        dx = (a * (y - x)) + (d * x * z)
        dy = (b * x) - (x * z) + (f * y)
        dz = (c * z) + (x * y) - (e * x * x)
        return dx, dy, dz
