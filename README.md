# 🧠 Edge Smoothing and Detection Using Diffusion-Based Methods

This repository demonstrates image smoothing and edge detection using two fundamental diffusion-based techniques:

- **Isotropic Diffusion** (Heat(Diffusion) Equation)
- **Anisotropic Diffusion** (Perona–Malik Model)

You’ll see how diffusion affects edge preservation and noise reduction, and how it impacts the performance of edge detectors like **Sobel**.

---

## 📸 Project Overview

Edge detection is a foundational task in image processing and computer vision. However, real-world images often contain noise that interferes with clean edge extraction. Diffusion-based smoothing helps address this:

| Method                 | Smoothing Behavior      | Edge Preservation |
|------------------------|-------------------------|--------------------|
| Isotropic Diffusion    | Uniform (blurs all)     | ❌ Blurs edges      |
| Anisotropic Diffusion  | Edge-aware (nonlinear)  | ✅ Preserves edges  |

---

## 🚀 Features

- ✅ **Isotropic smoothing** using the classical heat equation (Gaussian blur)
- ✅ **Anisotropic smoothing** using Perona–Malik diffusion
- ✅ **Sobel edge detection** on both smoothed results
- ✅ **Contour extraction** and visualization
- ✅ Easy-to-run code with visual comparisons

---

## How to Use 
1. Clone the repository and add your image adress(in the image = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE) line) that is to be sent for edge detection/smoothening .
2. Run the file .
3. One can see the example image within the folder for reference .


