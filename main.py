import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1_path = 'imgs/child.jpg'  # Path to the image file


#Read image function

def read_img(file_path):
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

#Edge Detection Function

def edge_detection(img, line_width, blur_amount):
    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Smooting noisy image using medianBlur
    gray_scale_img_blur = cv2.medianBlur(gray_scale_img, blur_amount)

    # Now detecting edges using adaptiveThreshold
    img_edges = cv2.adaptiveThreshold(gray_scale_img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_width, blur_amount)

    return img_edges

#Color Segmentation Function

def color_segmentation(img, k_value, epochs, accuracy):  # k_value is number of clusters    
    data = np.float32(img)
    data = data.reshape((-1, 3))
    
    # specifying stopping criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, epochs, accuracy)

    compactness, labels, centers = cv2.kmeans(data, k_value, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)

    result = centers[labels.flatten()]

    # reshaping image to its actual shape
    result = result.reshape(img.shape)

    return result

#Generate Cartoonize image function

def generate_cartoonize_img(img_path, LINE_WIDTH, BLUR_VALUE, TOTAL_COLORS, EPOCHS, ACCURACY):
    img = read_img(img_path)

    edgeImg = edge_detection(img, LINE_WIDTH, BLUR_VALUE)
    segmented_img = color_segmentation(img, TOTAL_COLORS, EPOCHS, ACCURACY)
    
    blurred_img = cv2.bilateralFilter(segmented_img, d=7, sigmaColor=200, sigmaSpace=200)    
    cartoonized_img = cv2.bitwise_and(blurred_img, blurred_img, mask = edgeImg)    
    
    return cartoonized_img

LINE_WIDTH  = 7
BLUR_VALUE = 5
TOTAL_COLORS = 6
EPOCHS = 50
ACCURACY = 0.02

cartoon_img_1 = generate_cartoonize_img(img_1_path, LINE_WIDTH, BLUR_VALUE, TOTAL_COLORS, EPOCHS, ACCURACY)

# Read original image
original_img = read_img(img_1_path)

# Ensure both images are the same size
cartoon_img_resized = cv2.resize(cartoon_img_1, (original_img.shape[1], original_img.shape[0]))

# Combine side by side
combined_img = np.hstack((original_img, cartoon_img_resized))

# Display the combined image
plt.figure(figsize=(10, 5))
plt.imshow(combined_img)
plt.axis('off')
plt.title("Original vs Cartoonized")
plt.show()