class FourWingsAttractor:
    def __init__(self) -> None:
        pass

    def derivatives(self, state):
        x, y, z = state
        a = 0.2
        c = -0.4
        b = 0.01
        dx = a * x + y * z
        dy = b * x + c * y - x * z
        dz = -z - x * y
        return dx, dy, dz

    def update(self, state, dt):
        x, y, z = state
        k1x, k1y, k1z = self.derivatives((x, y, z))
        k2x, k2y, k2z = self.derivatives(
            (
                x + 0.5 * dt * k1x,
                y + 0.5 * dt * k1y,
                z + 0.5 * dt * k1z,
            )
        )
        k3x, k3y, k3z = self.derivatives(
            (
                x + 0.5 * dt * k2x,
                y + 0.5 * dt * k2y,
                z + 0.5 * dt * k2z,
            )
        )
        k4x, k4y, k4z = self.derivatives(
            (
                x + dt * k3x,
                y + dt * k3y,
                z + dt * k3z,
            )
        )

        x_new = x + (dt / 6.0) * (k1x + 2.0 * k2x + 2.0 * k3x + k4x) 
        y_new = y + (dt / 6.0) * (k1y + 2.0 * k2y + 2.0 * k3y + k4y)
        z_new = z + (dt / 6.0) * (k1z + 2.0 * k2z + 2.0 * k3z + k4z)
        return x_new, y_new, z_new
