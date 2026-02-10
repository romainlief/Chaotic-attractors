from Attractor.chen import ChenAttractor
from Attractor.chua import ChuaAttractor
from Attractor.chenlee import ChenLeeAttractor
from Attractor.fourwings import FourWingsAttractor
from Attractor.sprott import SprottAttractor
from Attractor.threescroll import ThreeScrollAttractor
from Attractor.rabinovichfabrikant import RabinovichFabrikantAttractor
from Attractor.halvorsen import HalvorsenAttractor
from Attractor.rossler import RosslerAttractor
from Attractor.dadras import DadrasAttractor
from Attractor.langford import LangfordAttractor
from Attractor.thomas import ThomasAttractor
from Attractor.arneodo import ArneodoAttractor
from Attractor.sprottB import SprottBAttractor
from Attractor.sprottlinzf import SprottLinzFAttractor
from simulation import Simulation


def main():
    try:
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
        # attractor = ThomasAttractor()
        # attractor = ArneodoAttractor()
        # attractor = SprottBAttractor()
        attractor = SprottLinzFAttractor()

        sim = Simulation(attractor)

        initial_state = (0.1, 0, 0)  # Initial condition x, y, z
        dt = 0.03
        steps = 300_000

        states = sim.run(initial_state, dt, steps)
        # states = states[50000:]  # Discard initial transient for rabinovich-fabrikant

        sim.animate(
            states,
            interval=30,
            steps_per_frame=60,
            color_speed=10.0,
            cmap_name="hsv",
            line_width=1.0,
            rotate_camera=True,
            rotation_speed_deg=0.6,
            elevation_deg=55.0,
            rotate_y=False,
            rotation_speed_y_deg=0.4,
        )
    except KeyboardInterrupt:
        print("Simulation interrupted.")


if __name__ == "__main__":
    main()
