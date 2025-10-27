import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "gambar.jpg"   
image_rgb = cv2.imread(image_path)

if image_rgb is None:
    raise FileNotFoundError(f"Gambar '{image_path}' tidak ditemukan.")

image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv2.dilate(opening, kernel, iterations=3)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1  
markers[unknown == 255] = 0

image_color = image_rgb.copy()
markers_ws = cv2.watershed(image_color, markers)
image_color[markers_ws == -1] = [255, 0, 0]  

plt.figure(figsize=(14, 6))

plt.subplot(2, 3, 1)
plt.imshow(image_gray, cmap='gray')
plt.title("Citra Asli (Grayscale)")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(thresh, cmap='gray')
plt.title("Threshold (Otsu)")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(dist_transform, cmap='jet')
plt.title("Distance Transform")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(sure_fg, cmap='gray')
plt.title("Sure Foreground")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(sure_bg, cmap='gray')
plt.title("Sure Background")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title("Hasil Segmentasi Watershed")
plt.axis("off")

plt.tight_layout()
plt.show()