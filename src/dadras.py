from AAttractor.Aattractor import AAttractor

class DadrasAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 3
        c = 1.7
        b = 2.7
        d = 2
        e = 9
        dx = y - a * x + b * y * z
        dy = c * y - x * z + z
        dz = d * x * y - e * z
        return dx, dy, dz
