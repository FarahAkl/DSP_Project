# DSP_Project

# Cartoonize Image with OpenCV
This project uses OpenCV and K-Means clustering to cartoonize an image by combining edge detection with color segmentation.

## 🖼️ Example Output
Displays the original and cartoonized image side by side.

## 📂 Project Structure

```
.
├── imgs/
│   └── child.jpg              # Input image
├── main.py              # Main Python script
└── README.md                  # Project 

```
## 🚀 Features

**Edge Detection:** Uses adaptive thresholding for outlining.

**Color Segmentation:** Uses K-Means clustering to reduce the number of colors.

**Cartoon Effect:** Combines edge map and smoothed color segments for a cartoon look.

## 🛠️ Requirements

Install dependencies with:

```
pip install opencv-python numpy matplotlib

```

## 🧪 Parameters
You can tweak the effect by changing the following parameters:

LINE_WIDTH: Width of the edge lines (higher = thicker lines)

BLUR_VALUE: Blurring kernel for edge detection

TOTAL_COLORS: Number of color clusters for K-Means

EPOCHS: Max number of iterations for K-Means

ACCURACY: Convergence criteria for K-Means

## 📸 How It Works
Read Image – Loads and converts image from BGR to RGB.

Edge Detection – Converts to grayscale, applies median blur, then adaptive thresholding.

Color Segmentation – Flattens image and applies K-Means to reduce color palette.

Combine – Bilateral filter for smoothing + bitwise AND with edge mask.

🧾 Usage
Place your input image inside the imgs/ directory.

Update the image path in the script if needed:

```
img_1_path = 'imgs/child.jpg'

```

Run the script:

```
python main.py

```

The output will be displayed using matplotlib.

## 📌 Notes

The script currently processes a single image.

Make sure the image path exists and is correct.

## Team Members
 
 - Farah Hesham
 - Farida Elmekawey
 - Youmna Elgzery
 - Mariam Yasser
