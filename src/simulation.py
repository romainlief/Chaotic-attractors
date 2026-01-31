import matplotlib.pyplot as plt
from chen import ChenAttractor
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import matplotlib.cm as cm
import matplotlib.colors as colors

class Simulation:
    def __init__(self, attractor) -> None:
        self.attractor = attractor
        plt.style.use("dark_background")
        
    def run(self, initial_state, dt, steps):
        states = np.zeros((steps, 3))
        states[0] = initial_state
        for i in range(1, steps):
            prev = tuple(states[i - 1])
            
            new_state = self.attractor.update(prev, dt)
            states[i] = new_state
        return states
    
    def animate(self, states, interval=30, steps_per_frame: int = 10,
        color_speed: float = 10.0,
        cmap_name: str = "hsv",
        line_width: float = 1.0,):
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_axis_off()
        
        cmap = cm.get_cmap(cmap_name)
        finite_mask = np.all(np.isfinite(states), axis=1)
        finite_states = states[finite_mask]
        if finite_states.size == 0:
            finite_states = states[np.newaxis, 0]
        
        ax.set_xlim(left=(np.min(finite_states[:, 0]), np.max(finite_states[:, 0])))
        ax.set_ylim((np.min(finite_states[:, 1]), np.max(finite_states[:, 1])))
        ax.set_zlim((np.min(finite_states[:, 2]), np.max(finite_states[:, 2])))

        total_segs = max(finite_states.shape[0] - 1, 1)
        base_all = np.linspace(0.0, 1.0, total_segs, endpoint=False)
        colors_all = cmap(np.mod(color_speed * base_all, 1.0))

        init_end_idx = min(steps_per_frame, len(finite_states))
        init_segment = finite_states[:init_end_idx]
        if init_segment.shape[0] < 2:
            p = init_segment[0] if init_segment.shape[0] == 1 else finite_states[0]
            segs_init = np.array([[p, p]])
        else:
            segs_init = np.stack([init_segment[:-1], init_segment[1:]], axis=1)
        # Initialize collection with colors and add to axes
        collection = Line3DCollection(segs_init, linewidth=line_width)
        init_count = segs_init.shape[0]
        collection.set_color(colors_all[:init_count])
        ax.add_collection3d(collection)
        
        def update(frame):
            end_idx = min((frame + 1) * steps_per_frame, len(states))
            segment = states[:end_idx]
            # Keep only finite values for drawing
            finite_mask = np.all(np.isfinite(segment), axis=1)
            segment = segment[finite_mask]
            if segment.shape[0] < 2:
                # Keep a degenerate segment to maintain collection
                p = segment[0] if segment.shape[0] == 1 else finite_states[0]
                segs = np.array([[p, p]])
                collection.set_segments(segs)
                collection.set_color(cmap(np.array([0.0])))
                return (collection,)

            # Build 3D line segments and color by time index
            segs = np.stack([segment[:-1], segment[1:]], axis=1)  # shape (n-1, 2, 3)
            collection.set_segments(segs)
            # Use precomputed colors so prior segments keep their color
            collection.set_color(colors_all[: segs.shape[0]])
            return (collection,)

        total_frames = max(1, int(np.ceil(len(states) / steps_per_frame)))
        ani = FuncAnimation(
            fig, update, frames=total_frames, interval=interval, blit=False
        )
        plt.show()
