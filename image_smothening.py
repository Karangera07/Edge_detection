import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread("your_image", cv2.IMREAD_GRAYSCALE)
image = image.astype(np.float32) / 255.0  # Normalize to [0, 1]

# Heat equation parameters
alpha = 1       # Diffusion coefficient
dt = 0.1          # Time step
num_iter = 20     # Number of diffusion steps

# Copy image for processing
u = image.copy()

# Diffusion loop
for _ in range(num_iter):
    # Laplacian approximation
    laplacian = (
        np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) +
        np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) -
        4 * u
    )
    u += alpha * dt * laplacian


plt.figure(figsize=(12,4))
plt.title("Smoothened Image")
plt.imshow(u, cmap='gray')
plt.axis('off')
plt.show()

