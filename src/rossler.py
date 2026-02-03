from Aattractor import AAttractor


class RosslerAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 0.2
        c = 5.7
        b = 0.2
        dx = -(y + z)
        dy = x + a * y
        dz = b + z * (x - c)
        return dx, dy, dz
