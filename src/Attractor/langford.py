from Attractor.AAttractor.Aattractor import AAttractor


class LangfordAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 0.95
        c = 0.6
        b = 0.7
        d = 3.5
        e = 0.25
        f = 0.1
        dx = x * (z - b) - d * y
        dy = d * x + y * (z - b)
        dz = c + a * z - (z * z * z) / 3 - (x * x + y * y) * (1 + e * z)
        return dx, dy, dz
