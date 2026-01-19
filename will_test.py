import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Ball properties
x, y = 5, 5
vx, vy = 0.1, 0.15

ball, = ax.plot([], [], 'ro', markersize=12)

def init():
    ball.set_data([], [])
    return ball,

def update(frame):
    global x, y, vx, vy

    x += vx
    y += vy

    # Bounce off walls
    if x <= 0 or x >= 10:
        vx *= -1
    if y <= 0 or y >= 10:
        vy *= -1

    # pass sequences, not scalars
    ball.set_data([x], [y])
    return ball,

ani = animation.FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=300,
    interval=20,
    blit=True
)

plt.show()
