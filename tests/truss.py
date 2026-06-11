import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# параметры
N = 6
M = 10
x_vals = np.linspace(-10, 10, N+1)
y_vals = np.linspace(-20, 20, M+1)

def z(x, y):
    return x**2/40 - y**2/160 + 2.5

# шаг 1: узлы
nodes = {}
for i, xi in enumerate(x_vals):
    for j, yj in enumerate(y_vals):
        nodes[(i,j)] = (xi, yj, z(xi, yj))

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# шаг 2: балки вдоль x
for j in range(M+1):
    for i in range(N):
        p1 = nodes[(i,j)]
        p2 = nodes[(i+1,j)]
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
                color='steelblue', linewidth=0.8, alpha=0.4)

# шаг 3: балки вдоль y
for i in range(N+1):
    for j in range(M):
        p1 = nodes[(i,j)]
        p2 = nodes[(i,j+1)]
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
                color='steelblue', linewidth=0.8, alpha=0.4)

# шаг 4: прямолинейные образующие
t_values = [-2, -1, -0.5, 0.5, 1, 2]

def get_u_range(t, family=1):
    # находим u_min, u_max из условий -10<=x<=10, -20<=y<=20
    candidates = []
    sq40 = np.sqrt(40)
    sq160 = np.sqrt(160)
    if family == 1:
        # x = sq40/2*(t + u/t), y = sq160/2*(u/t - t)
        # из x: u/t = 2x/sq40 - t => u = t*(2x/sq40 - t)
        for xlim in [-10, 10]:
            candidates.append(t*(2*xlim/sq40 - t))
        # из y: u/t = 2y/sq160 + t => u = t*(2y/sq160 + t)
        for ylim in [-20, 20]:
            candidates.append(t*(2*ylim/sq160 + t))
    else:
        # x = sq40/2*(t + u/t), y = sq160/2*(t - u/t)
        # из x: u/t = 2x/sq40 - t => u = t*(2x/sq40 - t)
        for xlim in [-10, 10]:
            candidates.append(t*(2*xlim/sq40 - t))
        # из y: u/t = t - 2y/sq160 => u = t*(t - 2y/sq160)
        for ylim in [-20, 20]:
            candidates.append(t*(t - 2*ylim/sq160))
    return min(candidates), max(candidates)

for t in t_values:
    sq40 = np.sqrt(40)
    sq160 = np.sqrt(160)

    # семейство 1
    u_min, u_max = get_u_range(t, family=1)
    u_range = np.linspace(u_min, u_max, 50)
    xs = sq40/2*(t + u_range/t)
    ys = sq160/2*(u_range/t - t)
    zs = u_range + 2.5
    mask = (xs >= -10) & (xs <= 10) & (ys >= -20) & (ys <= 20)
    if mask.sum() > 1:
        ax.plot(xs[mask], ys[mask], zs[mask],
                color='red', linewidth=1.5, alpha=0.8)

    # семейство 2
    u_min, u_max = get_u_range(t, family=2)
    u_range = np.linspace(u_min, u_max, 50)
    xs = sq40/2*(t + u_range/t)
    ys = sq160/2*(t - u_range/t)
    zs = u_range + 2.5
    mask = (xs >= -10) & (xs <= 10) & (ys >= -20) & (ys <= 20)
    if mask.sum() > 1:
        ax.plot(xs[mask], ys[mask], zs[mask],
                color='orange', linewidth=1.5, alpha=0.8)

# шаг 5: контурные балки
for j in range(M):
    for xi, label in [(-10, 'left'), (10, 'right')]:
        p1 = (xi, y_vals[j], z(xi, y_vals[j]))
        p2 = (xi, y_vals[j+1], z(xi, y_vals[j+1]))
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
                color='black', linewidth=2)

for i in range(N):
    for yj, label in [(-20, 'front'), (20, 'back')]:
        p1 = (x_vals[i], yj, z(x_vals[i], yj))
        p2 = (x_vals[i+1], yj, z(x_vals[i+1], yj))
        ax.plot([p1[0],p2[0]], [p1[1],p2[1]], [p1[2],p2[2]],
                color='black', linewidth=2)

# шаг 6: опорные стойки
corners = [(-10,-20), (10,-20), (-10,20), (10,20)]
for cx, cy in corners:
    zc = z(cx, cy)
    ax.plot([cx,cx], [cy,cy], [0, zc], color='black', linewidth=3)
    ax.scatter([cx], [cy], [0], color='black', s=50, zorder=5)

# легенда
from matplotlib.lines import Line2D


ax.set_xlabel('x, м')
ax.set_ylabel('y, м')
ax.set_zlabel('z, м')
ax.view_init(elev=25, azim=-60)

plt.tight_layout()
plt.show()
print('done')