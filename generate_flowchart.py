import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure with white background
fig, ax = plt.subplots(1, 1, figsize=(14, 10), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors - professional research paper palette
color_main = '#E8F4F8'  # Light blue
color_process = '#FFFFFF'  # White
color_accent = '#4A4A4A'  # Dark gray
color_border = '#2C3E50'  # Dark blue-gray
color_text = '#1C1C1C'  # Almost black
color_annotation = '#34495E'  # Medium gray

# Helper function to create rounded box
def create_box(ax, x, y, width, height, text, color=color_process, fontsize=11, fontweight='normal'):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.1", 
                         edgecolor=color_border, facecolor=color,
                         linewidth=2.5, zorder=10)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
            fontweight=fontweight, color=color_text, zorder=11)

# Helper function to create arrow
def create_arrow(ax, x1, y1, x2, y2, style='->'):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle=style, mutation_scale=25, 
                           color=color_border, linewidth=2.5, zorder=5)
    ax.add_patch(arrow)

# Helper function to create annotation box
def create_annotation(ax, x, y, width, height, text, fontsize=9):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.08", 
                         edgecolor=color_annotation, facecolor='#F9F9F9',
                         linewidth=1.5, linestyle='--', zorder=8)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=color_annotation, zorder=9, style='italic', multialignment='center')

# Title
ax.text(5, 9.5, 'CNN Model Training with SAM Optimization', 
        ha='center', va='top', fontsize=16, fontweight='bold', color=color_text)

# Main flow - LEFT COLUMN
y_start = 8.8
create_box(ax, 2.5, y_start, 1.8, 0.5, 'Input Data', fontsize=11, fontweight='bold')

create_arrow(ax, 2.5, y_start - 0.25, 2.5, y_start - 0.7)
create_box(ax, 2.5, y_start - 1.1, 1.8, 0.5, 'Pre-processing', fontsize=11, fontweight='bold')

create_arrow(ax, 2.5, y_start - 1.35, 2.5, y_start - 1.8)
create_box(ax, 2.5, y_start - 2.2, 1.8, 0.5, 'CNN Model', fontsize=11, fontweight='bold')

create_arrow(ax, 2.5, y_start - 2.45, 2.5, y_start - 2.9)
create_box(ax, 2.5, y_start - 3.3, 1.8, 0.5, 'Training', fontsize=11, fontweight='bold')

create_arrow(ax, 2.5, y_start - 3.55, 2.5, y_start - 4.0)
create_box(ax, 2.5, y_start - 4.4, 1.8, 0.5, 'Evaluate\nPerformance', fontsize=10, fontweight='bold')

# SAM Optimization section - MIDDLE
create_box(ax, 5, y_start - 2.2, 2.0, 0.5, 'SAM Optimization', fontsize=11, fontweight='bold')

# Connect CNN to SAM
create_arrow(ax, 3.4, y_start - 2.2, 4.0, y_start - 2.2)

# SAM to Output
create_arrow(ax, 5, y_start - 1.95, 5, y_start - 1.5)
create_box(ax, 5, y_start - 1.1, 1.8, 0.5, 'Output', fontsize=11, fontweight='bold')

# SAM process boxes - MIDDLE
create_box(ax, 5, y_start - 3.0, 2.0, 0.5, 'Compute Loss\nFunction', fontsize=10, fontweight='bold')
create_arrow(ax, 5, y_start - 2.45, 5, y_start - 3.25)

create_box(ax, 5, y_start - 3.8, 2.0, 0.5, 'Update\nParameters', fontsize=10, fontweight='bold')
create_arrow(ax, 5, y_start - 3.55, 5, y_start - 4.05)

# Connect Training to Compute Loss
create_arrow(ax, 3.4, y_start - 4.4, 4.0, y_start - 3.0)

# Connect Update Parameters to Evaluate Performance
create_arrow(ax, 4.0, y_start - 3.8, 3.4, y_start - 4.4)

# Feedback loop
create_arrow(ax, 2.5, y_start - 4.65, 2.5, y_start - 5.1)
loop_x = 2.5 - 1.2
create_arrow(ax, 2.5, y_start - 5.1, loop_x, y_start - 5.1)
create_arrow(ax, loop_x, y_start - 5.1, loop_x, y_start - 3.3)
create_arrow(ax, loop_x, y_start - 3.3, 2.5 - 0.9, y_start - 3.3)

# RIGHT SIDE ANNOTATIONS
# Main process description
create_annotation(ax, 7.8, y_start - 0.5, 1.8, 1.0,
                 'SAM Optimization:\nPerturbs CNN\nparameters to\nminimize\nsharpness',
                 fontsize=8.5)

create_annotation(ax, 7.8, y_start - 2.5, 1.8, 0.8,
                 'Loss at\nperturbation\nfor sharpness\nevaluation',
                 fontsize=8.5)

create_annotation(ax, 7.8, y_start - 3.8, 1.8, 0.8,
                 'Parameters\nupdated via\nsharpness-aware\ngradient',
                 fontsize=8.5)

create_annotation(ax, 7.8, y_start - 4.8, 1.8, 0.8,
                 'Generalization\nperformance\nevaluation',
                 fontsize=8.5)

# LEFT SIDE INITIALIZATION DETAILS
create_annotation(ax, 0.7, y_start - 3.0, 1.6, 0.9,
                 'Initialize SAM\nperturbation\nparameters',
                 fontsize=8.5)

create_annotation(ax, 0.7, y_start - 4.2, 1.6, 0.9,
                 'Approximate\nworst-case\nperturbation',
                 fontsize=8.5)

# Add legend-style box at bottom
legend_y = 0.5
ax.text(0.5, legend_y + 0.3, 'Methodology:', fontsize=10, fontweight='bold', color=color_text)
ax.text(0.5, legend_y - 0.2, '• Iterative training with SAM-based parameter updates', 
        fontsize=9, color=color_annotation)
ax.text(0.5, legend_y - 0.6, '• Sharpness-aware optimization for improved generalization', 
        fontsize=9, color=color_annotation)

plt.tight_layout()
plt.savefig('CNN_SAM_Flowchart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Flowchart saved as 'CNN_SAM_Flowchart.png'")
plt.show()
