from chen import ChenAttractor
from chua import ChuaAttractor
from chenlee import ChenLeeAttractor
from simulation import Simulation

def main():
    #attractor = ChenAttractor()
    #attractor = ChuaAttractor()
    attractor = ChenLeeAttractor()
    sim = Simulation(attractor)
    
    initial_state = (1, 1, 0) # Initial condition x, y, z
    dt = 0.003
    steps = 100000
    
    states = sim.run(initial_state, dt, steps)
    
    sim.animate(states, interval=35, steps_per_frame=50,
                color_speed=20.0,
                cmap_name="hsv",
                line_width=1.0)

if __name__ == "__main__":
    main()