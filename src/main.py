from chen import ChenAttractor
from chua import ChuaAttractor
from chenlee import ChenLeeAttractor
from fourwings import FourWingsAttractor
from sprott import SprottAttractor
from threescroll import ThreeScrollAttractor

from simulation import Simulation


def main():
    # attractor = ChenAttractor()
    # attractor = ChuaAttractor()
    # attractor = ChenLeeAttractor()
    # attractor = FourWingsAttractor()
    # attractor = SprottAttractor()
    attractor = ThreeScrollAttractor()

    sim = Simulation(attractor)

    initial_state = (-0.29, -0.25, -0.59)  # Initial condition x, y, z
    dt = 0.001
    steps = 100000

    states = sim.run(initial_state, dt, steps)

    sim.animate(
        states,
        interval=30,
        steps_per_frame=10,
        color_speed=10.0,
        cmap_name="hsv",
        line_width=1.0,
        rotate_camera=True,
        rotation_speed_deg=0.8,
        elevation_deg=10.0,
        rotate_y=False,
        rotation_speed_y_deg=0.4,
    )


if __name__ == "__main__":
    main()
