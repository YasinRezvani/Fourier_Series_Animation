import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A0 = 3
omega0 = np.pi / 2

def a_n(n):
    return (6 / (n * np.pi)) * np.sin(n * np.pi / 2)

def b_n(n):
    return 0

def fourier_series(x, n_terms):
    result = A0 / 2
    for n in range(1, n_terms + 1):
        result += a_n(n) * np.cos(n * omega0 * x) + b_n(n) * np.sin(n * omega0 * x)
    return result

x = np.linspace(-10, 10, 2000)

fig, ax = plt.subplots(figsize=(8, 4))
line, = ax.plot(x, fourier_series(x, 1), color='blue')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.grid(True)

legend_box = ax.text(0.95, 0.95, '', transform=ax.transAxes, va='top', ha='right', 
                     bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.5'), 
                     fontsize=12, weight='bold')

colors = plt.cm.jet(np.linspace(0, 1, 50))

def update(n):
    y = fourier_series(x, n + 1)
    line.set_ydata(y)
    line.set_color(colors[n % len(colors)])
    legend_box.set_text(f'n = {n + 1}')
    
    return line, legend_box

speed = 1

ani = animation.FuncAnimation(fig, update, frames=range(50), blit=True, repeat=False, interval=1000/speed)

ani.save('fourier_series.gif', writer='pillow', fps=speed)

plt.show()
