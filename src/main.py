from chen import ChenAttractor
from chua import ChuaAttractor
from chenlee import ChenLeeAttractor
from fourwings import FourWingsAttractor
from simulation import Simulation


def main():
    # attractor = ChenAttractor()
    # attractor = ChuaAttractor()
    # attractor = ChenLeeAttractor()
    attractor = FourWingsAttractor()

    sim = Simulation(attractor)

    initial_state = (1.3, -0.18, 0.01)  # Initial condition x, y, z
    dt = 0.09
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
        elevation_deg=25.0,
        rotate_y=True,
        rotation_speed_y_deg=0.7,
    )


if __name__ == "__main__":
    main()
