import matplotlib.pyplot as plt
from random import randrange

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

colors = [(255, 0, 0), (220, 65, 97), (200, 100, 150), (177, 129, 110), (160, 150, 80), (101, 188, 122), (20, 240, 180), (19, 231, 183), (10, 116, 219), (0, 0, 255)]

for i, color in enumerate(colors):
    # r, g, b = randrange(256), randrange(256), randrange(256)
    r, g, b = color[0], color[1], color[2]

    ax.scatter(r, g, b, color=f"#{r:02x}{g:02x}{b:02x}", s=1000)
    if i < len(colors)-1:
        ax.plot([r, colors[i+1][0]], [g, colors[i+1][1]], [b, colors[i+1][2]], 'ko-')

ax.set_xlabel('RED', fontweight='bold')
ax.set_ylabel('GREEN', fontweight='bold')
ax.set_zlabel('BLUE', fontweight='bold')

ax.text(255, 0, 30, "STARTING COLOR", fontsize=14, fontweight='bold', backgroundcolor='yellow')
ax.text(0, 0, 282, "ENDING COLOR", fontsize=14, fontweight='bold', backgroundcolor='yellow')

ax.xaxis.label.set_color('red')
ax.yaxis.label.set_color('green')
ax.zaxis.label.set_color('blue')

ax.set_xlim([0, 255])
ax.set_ylim([0, 255])
ax.set_zlim([0, 255])

ax.invert_yaxis()

ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='green')
ax.tick_params(axis='z', colors='blue')

ax.set_title('Output colors', fontsize=26, y=-0.075)

plt.show()

# fig.savefig('output_x_colors.png')
