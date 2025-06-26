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

##  How to Use 
1. Clone the repository .
2. edge_detection.py and anisotropic_diffusion.py first smoothen the image and then detects the edges and gives contour plot.
3. Add your image adress(in the image = cv2.imread("your_image", cv2.IMREAD_GRAYSCALE) line) that is to be sent for edge detection/smoothening .
4. One can change the number of iterations in case of smoothening more iterations means more blurring hence only prominent edges appear after edge_detection .
5. Another way is to tune value of "k" in anisotropic diffusion , lower the k , higher is the sensitivity to edges .
6. Run the file .
7. One can see the example image within the folder for reference .


