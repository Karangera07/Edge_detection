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


sobel_x = cv2.Sobel(u, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(u, cv2.CV_64F, 0, 1, ksize=3)
edges = np.hypot(sobel_x, sobel_y)

# Normalize and convert to 8-bit
edges_norm = (edges / np.max(edges) * 255).astype(np.uint8)

# Threshold to get binary edge map
_, binary_edges = cv2.threshold(edges_norm, 50, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank canvas or original image
contour_img = np.zeros_like(edges_norm)
cv2.drawContours(contour_img, contours, -1, 255, 1)

plt.figure(figsize=(12,4))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(u, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Edge Map")
plt.imshow(edges_norm, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Contour Plot")
plt.imshow(contour_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig("edge_detection_using_heat_equation")
plt.show()