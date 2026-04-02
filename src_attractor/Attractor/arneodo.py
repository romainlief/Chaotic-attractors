from Attractor.AAttractor.Aattractor import AAttractor


class ArneodoAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        a = -5.5
        b = 3.5
        c = -1.0
        dx = y
        dy = z
        dz = -a * x - b * y - z + c * x * x * x
        return dx, dy, dz
