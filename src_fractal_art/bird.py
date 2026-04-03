import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

N = 9830
k = np.arange(1, N + 1)

# --- X(k) ---
X = (
    (np.sin(np.pi * k / 20000)) ** 12
    * (
        (1 / 2) * (np.cos(31 * np.pi * k / 10000)) ** 16 * np.sin(6 * np.pi * k / 10000)
        + (1 / 6) * (np.sin(31 * np.pi * k / 10000)) ** 20
    )
    + 3 * k / 20000
    + (np.cos(31 * np.pi * k / 10000)) ** 6
    * np.sin(np.pi / 2 * ((k - 10000) / 10000) ** 7 - np.pi / 5)
)

# --- Y(k) ---
Y = (
    -9
    / 4
    * (np.cos(31 * np.pi * k / 10000)) ** 6
    * np.cos(np.pi / 2 * ((k - 10000) / 10000) ** 7 - np.pi / 5)
    * (2 / 3 + (np.sin(np.pi * k / 20000) * np.sin(3 * np.pi * k / 20000)) ** 6)
    + 3
    / 4
    * (np.cos(3 * np.pi * (k - 10000) / 100000)) ** 10
    * (np.cos(9 * np.pi * (k - 10000) / 100000)) ** 10
    * (np.cos(36 * np.pi * (k - 10000) / 100000)) ** 14
    + 7 / 10 * ((k - 10000) / 10000) ** 2
)

# --- R(k) ---
R = (np.sin(np.pi * k / 20000)) ** 10 * (
    (1 / 4) * (np.cos(31 * np.pi * k / 10000 + 25 * np.pi / 32)) ** 20
    + (1 / 20) * (np.cos(31 * np.pi * k / 10000)) ** 2
    + 1 / 30 * (3 / 2 - (np.cos(62 * np.pi * k / 10000)) ** 2)
)

# --- Calcul des limites à l'avance ---
margin = max(R) * 2
x_min, x_max = X.min() - margin, X.max() + margin
y_min, y_max = Y.min() - margin, Y.max() + margin

# Les tres petits cercles deviennent quasi invisibles avec un trait sous-pixel.
# On garde la meme geometrie mais on adapte legerement l'epaisseur de trait.
r_norm = R / R.max()
linewidths = 0.01 + 0.82 * ((1.0 - r_norm) ** 5)

# --- Setup figure ---
fig, ax = plt.subplots(figsize=(3, 3), dpi=140)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor("white")

# On ralentit le debut pour rendre visibles les premieres structures,
# puis on accelere progressivement pour garder une animation fluide.
n_frames = 220
t = np.linspace(0.0, 1.0, n_frames + 1)
draw_counts = np.floor(N * (t**1.8)).astype(int)
draw_counts[0] = 0
draw_counts[-1] = N
draw_counts = np.maximum.accumulate(draw_counts)


def animate(frame):
    start = draw_counts[frame]
    end = draw_counts[frame + 1]

    # Ajouter seulement les nouveaux cercles sans redessiner
    for i in range(start, end):
        circle = Circle(
            (X[i], Y[i]),
            R[i],
            color="black",
            fill=False,
            linewidth=float(linewidths[i]),
            clip_on=False,
        )
        ax.add_patch(circle)
    return ax.patches


ani = animation.FuncAnimation(
    fig,
    animate,
    frames=n_frames,
    interval=16,  # millisecondes entre chaque frame (~60 FPS)
    repeat=False,
)

plt.show()
