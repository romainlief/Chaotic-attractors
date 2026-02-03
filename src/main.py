from chen import ChenAttractor
from chua import ChuaAttractor
from chenlee import ChenLeeAttractor
from fourwings import FourWingsAttractor
from sprott import SprottAttractor
from threescroll import ThreeScrollAttractor
from rabinovichfabrikant import RabinovichFabrikantAttractor
from halvorsen import HalvorsenAttractor
from rossler import RosslerAttractor
from dadras import DadrasAttractor
from langford import LangfordAttractor
from thomas import ThomasAttractor
from simulation import Simulation


def main():
    # attractor = ChenAttractor()
    # attractor = ChuaAttractor()
    # attractor = ChenLeeAttractor()
    # attractor = FourWingsAttractor()
    # attractor = SprottAttractor()
    # attractor = ThreeScrollAttractor()
    # attractor = RabinovichFabrikantAttractor()
    # attractor = HalvorsenAttractor()
    # attractor = RosslerAttractor()
    # attractor = DadrasAttractor()
    # attractor = LangfordAttractor()
    attractor = ThomasAttractor()

    sim = Simulation(attractor)

    initial_state = (2.0, -1.0, 0.5)  # Initial condition x, y, z
    dt = 0.03
    steps = 300_000

    states = sim.run(initial_state, dt, steps)
    # states = states[50000:]  # Discard initial transient for rabinovich-fabrikant

    sim.animate(
        states,
        interval=30,
        steps_per_frame=300,
        color_speed=10.0,
        cmap_name="hsv",
        line_width=1.0,
        rotate_camera=True,
        rotation_speed_deg=1.5,
        elevation_deg=5.0,
        rotate_y=False,
        rotation_speed_y_deg=0.4,
    )


if __name__ == "__main__":
    main()
