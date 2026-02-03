from Aattractor import AAttractor

class FourWingsAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = 0.2
        c = -0.4
        b = 0.01
        dx = a * x + y * z
        dy = b * x + c * y - x * z
        dz = -z - x * y
        return dx, dy, dz
