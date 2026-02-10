from AAttractor.Aattractor import AAttractor


class ThreeDQuadraticAttractor(AAttractor):
    def __init__(self) -> None:
        super().__init__()
        self.is_discrete = True

    def derivatives(self, state):
        x, y, z = state
        a0 = -0.875
        a1 = -0.173
        a2 = 0.307
        a3 = -0.436
        a4 = 0.598
        a5 = 0.003
        a6 = 0.039
        a7 = 0.96
        a8 = -0.84
        a9 = 0.885
        a10 = 0.774
        a11 = 0.281
        a12 = -0.015
        a13 = 0.585
        a14 = 0.442
        a15 = -0.18
        a16 = -0.535
        a17 = -0.151
        a18 = -0.971
        a19 = -0.48
        a20 = 0.777
        a21 = 0.418
        a22 = 0.185
        a23 = 0.006
        a24 = 0.45
        a25 = -0.066
        a26 = 0.498
        a27 = 0.142
        a28 = -0.246
        a29 = -0.939
        xn = (
            a0
            + a1 * x
            + a2 * y
            + a3 * z
            + a4 * x * y
            + a5 * x * z
            + a6 * y * z
            + a7 * x * x
            + a8 * y * y
            + a9 * z * z
        )
        yn = (
            a10
            + a11 * x
            + a12 * y
            + a13 * z
            + a14 * x * y
            + a15 * x * z
            + a16 * y * z
            + a17 * x * x
            + a18 * y * y
            + a19 * z * z
        )
        zn = (
            a20
            + a21 * x
            + a22 * y
            + a23 * z
            + a24 * x * y
            + a25 * x * z
            + a26 * y * z
            + a27 * x * x
            + a28 * y * y
            + a29 * z * z
        )
        return xn, yn, zn

    # This system is a discrete 3D quadratic map (n -> n+1),
    # not a continuous-time ODE. Override update to perform
    # a single iteration step and ignore dt.
    def update(self, state, dt):  # dt is unused for maps
        return self.derivatives(state)
