import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import numpy as np

# ---------------------------
# Zig-Zag Sort Function
# ---------------------------
def zig_zag_sort(arr, steps):
    # Add initial step: just display the array
    steps.append((arr.copy(), -1, -1, "Initial State", -1))

    flag = True
    for i in range(len(arr) - 1):
        steps.append((arr.copy(), i, i + 1, "Compare", 2))
        if flag:
            steps.append((arr.copy(), i, i + 1, "Check if a[i] > a[i+1]", 3))
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                steps.append((arr.copy(), i, i + 1, "Swap", 4))
        else:
            steps.append((arr.copy(), i, i + 1, "Check if a[i] < a[i+1]", 6))
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                steps.append((arr.copy(), i, i + 1, "Swap", 7))
        steps.append((arr.copy(), i, i + 1, "Toggle flag", 8))
        flag = not flag
    steps.append((arr.copy(), -1, -1, "Done", -1))

# ---------------------------
# Pseudo-code Lines
# ---------------------------
pseudo_lines = [
    "1. for i in range(len(arr) - 1):",
    "2.     if flag:",
    "3.         if arr[i] > arr[i+1]:",
    "4.             swap(arr[i], arr[i+1])",
    "5.     else:",
    "6.         if arr[i] < arr[i+1]:",
    "7.             swap(arr[i], arr[i+1])",
    "8.     flag = not flag"
]

# ---------------------------
# Animation Setup
# ---------------------------
fig = plt.figure(figsize=(14, 7))
gs = fig.add_gridspec(3, 2, width_ratios=[2, 1], height_ratios=[3, 1, 0.8])

ax_bar = fig.add_subplot(gs[0, 0])
ax_array = fig.add_subplot(gs[1, 0])
ax_buttons = fig.add_subplot(gs[2, 0])
ax_buttons.axis('off')

# Code Box Setup
ax_code = fig.add_subplot(gs[:, 1])
ax_code.axis('off')
code_texts = []
for i, line in enumerate(pseudo_lines):
    txt = ax_code.text(0.05, 1 - i * 0.1, line, fontsize=12, ha='left', va='top')
    code_texts.append(txt)

# Initialize bars and array values
arr = np.random.randint(10, 100, size=10)
bars = ax_bar.bar(range(len(arr)), arr, color='lightblue')
ax_bar.set_title("Zig-Zag Sorting Visualization")
ax_bar.set_ylim(0, max(arr) + 20)

array_texts = [
    ax_array.text(i, 0.5, f"{arr[i]}", fontsize=12,
                  ha='center', va='center', bbox=dict(facecolor='lightblue', boxstyle='round,pad=0.3'))
    for i in range(len(arr))
]

index_texts = [
    ax_array.text(i, 0.2, str(i), fontsize=10, ha='center', va='top')
    for i in range(len(arr))
]

ax_array.set_xlim(-1, len(arr))
ax_array.set_ylim(0, 1)
ax_array.axis('off')

# Sorting Steps
steps = []
zig_zag_sort(arr.copy(), steps)
step_text = ax_bar.text(0.02, 0.95, "", transform=ax_bar.transAxes, fontsize=12, verticalalignment='top')
current_step = [0]
ani = None

# ---------------------------
# Code Highlighting
# ---------------------------
def highlight_code(line_num):
    for i, txt in enumerate(code_texts):
        txt.set_color("black")
        txt.set_fontweight("normal")
        if i == line_num - 1:
            txt.set_color("red")
            txt.set_fontweight("bold")

# ---------------------------
# Update Function
# ---------------------------
def update(frame):
    a, i, j, action, code_line = steps[frame]

    # Update bars
    for idx, b in enumerate(bars):
        b.set_height(a[idx])
        b.set_color("lightblue")
    for idx, t in enumerate(array_texts):
        t.set_text(f"{a[idx]}")
        t.set_bbox(dict(facecolor='lightblue', boxstyle='round,pad=0.3'))

    if i >= 0:
        bars[i].set_color("orange")
        bars[j].set_color("red")
        array_texts[i].set_bbox(dict(facecolor='orange', boxstyle='round,pad=0.3'))
        array_texts[j].set_bbox(dict(facecolor='red', boxstyle='round,pad=0.3'))

    step_text.set_text(f"{action} a[{i}] and a[{j}]" if i >= 0 else "Initial State")
    current_step[0] = frame

    # Highlight pseudo-code
    if code_line != -1:
        highlight_code(code_line)
    else:
        for txt in code_texts:
            txt.set_color("black")
            txt.set_fontweight("normal")

# ---------------------------
# Button Functions
# ---------------------------
def play(event):
    global ani
    ani = animation.FuncAnimation(
        fig, update,
        frames=range(current_step[0], len(steps)),
        interval=1500,
        repeat=False
    )
    plt.draw()

def reset(event):
    global ani
    if ani:
        ani.event_source.stop()
    current_step[0] = 0
    update(0)
    plt.draw()

def stop(event):
    global ani
    if ani:
        ani.event_source.stop()

# ---------------------------
# Buttons
# ---------------------------
axplay = plt.axes([0.55, 0.05, 0.1, 0.05])
axstop = plt.axes([0.44, 0.05, 0.1, 0.05])
axreset = plt.axes([0.33, 0.05, 0.1, 0.05])

bplay = Button(axplay, 'Play')
bplay.on_clicked(play)

bstop = Button(axstop, 'Stop')
bstop.on_clicked(stop)

breset = Button(axreset, 'Reset')
breset.on_clicked(reset)

# Initial Step Display
update(0)
plt.tight_layout()
plt.show()