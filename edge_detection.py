import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread('flower.webp', cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32) / 255.0

# Apply anisotropic diffusion
def anisotropic_diffusion(img, n_iter=20, k=50, lamb=0.25):
    for _ in range(n_iter):
        north = np.roll(img, -1, axis=0) - img
        south = np.roll(img, 1, axis=0) - img
        east = np.roll(img, -1, axis=1) - img
        west = np.roll(img, 1, axis=1) - img

        c_n = np.exp(-(north / k) ** 2)
        c_s = np.exp(-(south / k) ** 2)
        c_e = np.exp(-(east / k) ** 2)
        c_w = np.exp(-(west / k) ** 2)

        img += lamb * (c_n * north + c_s * south + c_e * east + c_w * west)

    return img

# Apply diffusion and Sobel edge detection
diffused = anisotropic_diffusion(img, n_iter=20, k=20, lamb=0.25)
sobel_x = cv2.Sobel(diffused, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(diffused, cv2.CV_64F, 0, 1, ksize=3)
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

# Plotting
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
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
plt.savefig("edge_detection_using_anisotropic")
plt.show()
