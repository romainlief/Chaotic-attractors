from AAttractor.Aattractor import AAttractor


class RabinovichFabrikantAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()

    def derivatives(self, state):
        x, y, z = state
        alpha = 0.05
        gamma = 0.10
        dx = y * (z - 1 + (x * x)) + (gamma * x)
        dy = x * ((3 * z) + 1 - (x * x)) + (gamma * y)
        dz = -2 * z * (alpha + (x * y))
        return dx, dy, dz
