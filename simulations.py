import matplotlib.pyplot as plt
import numpy as np

# Number of temporal branches
n_branches = 5
x = np.linspace(0, 10, 100)  # timeline
colors = plt.cm.viridis(np.linspace(0, 1, n_branches))

plt.figure(figsize=(8,5))

# Plot temporal branches as curves
for i, c in enumerate(colors):
    y = np.sin(x + i*np.pi/10) + i*0.5
    plt.plot(x, y, color=c, label=f'Branch {i+1}', linewidth=2)

# Highlight observer branch
plt.plot(x, np.sin(x + 2*np.pi/10) + 2*0.5, color='red', linewidth=3, label='Observer Branch')

plt.xlabel("Temporal Field Coordinate")
plt.ylabel("Branch Value / Amplitude")
plt.title("Temporal Field with Multiple Branches")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
##################################################################################
# Figure 2

import matplotlib.pyplot as plt
import numpy as np

# Pre-measurement density matrix (example 2x2)
rho_pre = np.array([[0.6, 0.3],
                    [0.3, 0.4]])

# Post-measurement density matrix (observer collapses to branch 0)
rho_post = np.array([[1, 0],
                     [0, 0]])

fig, axs = plt.subplots(1, 2, figsize=(10,4))

# Pre-measurement
im0 = axs[0].imshow(rho_pre, cmap='viridis', vmin=0, vmax=1)
axs[0].set_title("Observer Density Matrix (Pre-Measurement)")
axs[0].set_xticks([])  # remove x-axis ticks
axs[0].set_yticks([])  # remove y-axis ticks
for i in range(2):
    for j in range(2):
        axs[0].text(j, i, f"{rho_pre[i,j]:.2f}", ha='center', va='center', color='white')

# Post-measurement
im1 = axs[1].imshow(rho_post, cmap='viridis', vmin=0, vmax=1)
axs[1].set_title("Observer Density Matrix (Post-Measurement)")
axs[1].set_xticks([])  # remove x-axis ticks
axs[1].set_yticks([])  # remove y-axis ticks
for i in range(2):
    for j in range(2):
        axs[1].text(j, i, f"{rho_post[i,j]:.2f}", ha='center', va='center', color='white')

plt.tight_layout()
plt.show()

##################################################################################
# Figure 3

# Qubit amplitudes (example)
alpha0 = 0.8
alpha1 = 0.6

# Pre-measurement density matrix
rho_pre = np.array([[abs(alpha0)**2, alpha0*np.conj(alpha1)],
                    [alpha1*np.conj(alpha0), abs(alpha1)**2]])

# Post-measurement density matrices
rho_post_0 = np.array([[1, 0],
                       [0, 0]])
rho_post_1 = np.array([[0, 0],
                       [0, 1]])

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

cmap = 'viridis'

im0 = axs[0].imshow(rho_pre.real, cmap=cmap)
axs[0].set_title('Pre-Measurement')
axs[0].axis('off')
fig.colorbar(im0, ax=axs[0])

im1 = axs[1].imshow(rho_post_0, cmap=cmap)
axs[1].set_title('Post-Measurement: Branch 0')
axs[1].axis('off')
fig.colorbar(im1, ax=axs[1])

im2 = axs[2].imshow(rho_post_1, cmap=cmap)
axs[2].set_title('Post-Measurement: Branch 1')
axs[2].axis('off')
fig.colorbar(im2, ax=axs[2])

plt.tight_layout()
plt.show()
