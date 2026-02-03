from Aattractor import AAttractor


class ChenLeeAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 5
        c = -0.38
        b = -10
        dx = a * x - y * z
        dy = b * y + x * z
        dz = c * z + (x * y * 1 / 3)
        return dx, dy, dz
