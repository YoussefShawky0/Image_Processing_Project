# Digital Image Processing

## Overview

This project provides functionality to enhance or transform images through various filters and transformations, focusing on tasks like noise reduction, edge detection, and intensity adjustment. Below is a detailed explanation of the components, filters, and functionality.

---

## Features

1. **Upload and Display**:
    - Upload an image through the interface.
    - View the original image in a designated canvas.
2. **Filters**:
    - Apply a variety of filters to enhance or transform the image.
3. **Before and After Canvases**:
    - Compare the original image and the processed image side by side.
4. **Histogram**:
    - Display the image histogram to analyze pixel intensity distribution.
5. **Buttons**:
    - **Reset**: Reverts the image to its original state.
    - **Upload**: Uploads a new image.
    - **Apply**: Applies the selected filter to the image.
    - **Save**: Saves the processed image to the disk.
    - **Select Filter**: Dropdown or selection to choose the desired filter.
    - **Conditional Rendering**:
        - **K-Means**: Option to apply K-Means clustering.
        - **Periodic Noise Direction**: Option to select the direction for periodic noise filtering.

---

## Filters

### 1. **Median Filter**

- **Description**: Reduces noise by replacing each pixel value with the median value of its neighbors. Useful for **noise reduction**, particularly salt-and-pepper noise.
    
   ![image](https://github.com/user-attachments/assets/ff1c35ad-a3c8-47f3-9155-8de90e1b5a1a)

    

### 2. **Averaging Filter**

- **Description**: Smoothens the image by averaging pixel values in a kernel. Effective for **blurring** and reducing random noise.
    
  ![image](https://github.com/user-attachments/assets/ee9fce61-0972-4b81-a143-10a60a484dc9)
    

### 3. **Low-Pass Filters**

- **Description**: Removes high-frequency noise while preserving low-frequency details. Ideal for **noise suppression** and overall smoothing.
    
   ![image](https://github.com/user-attachments/assets/f486bf6e-7b39-4b14-8857-00dcb4d36111)

    

### 4. **Canny Edge Detection**

- **Description**: Detects edges in an image by finding areas of rapid intensity change. Suitable for **edge detection** tasks.
    
   ![image](https://github.com/user-attachments/assets/ee1d4b77-1749-42a2-a721-09a763a7d072)

    

### 5. **Periodic Noise Filter**

- **Description**: Removes periodic noise patterns from the image. Useful for **noise reduction** in images with repeating patterns of distortion.
    
   ![image](https://github.com/user-attachments/assets/46d1c74c-5550-4878-a035-ebb4f6f7f59e)

    

### 6. **RGB to Grayscale**

- **Description**: Converts the image from RGB color space to grayscale. Often used for simplifying images by reducing them to **intensity-based representations**.
    
   ![image](https://github.com/user-attachments/assets/f3d6a9c1-036d-4247-9922-71f86714d9e7)

    

---

## Model

### **K-Means Clustering**

- **Description**: Groups similar pixel values into clusters to simplify and segment images. In this project, it is designed to work with datasets consisting of numbers between 0 and 9, and the algorithm is responsible for **predicting the numbers** based on clustering.
    
    ![image](https://github.com/user-attachments/assets/3665cbfc-7b2e-430d-849d-079850bc21b3)

    

---

## Interface Components

### Buttons:

1. **Reset**:
    - Clears all applied filters and resets the image to its original state.
2. **Upload**:
    - Opens a file dialog to upload a new image.
3. **Apply**:
    - Executes the selected filter on the uploaded image.
4. **Save**:
    - Saves the processed image in the desired format.
5. **Select Filter**:
    - Dropdown or radio buttons to choose the filter to be applied.

### Canvases:

1. **Before Canvas**:
    - Displays the original image.
2. **After Canvas**:
    - Displays the processed image.
3. **Histogram Canvas**:
    - Plots the histogram of the image for pixel intensity analysis.

### Conditional Rendering:

- **K-Means Clustering**:
    - Allows the user to cluster image colors into groups for classification (unsupervised).
- **Periodic Noise Direction**:
    - Provides options to select the direction for periodic noise filtering.

---

## Workflow

1. **Upload an Image**:
    - Use the "Upload" button to load an image into the application.
2. **Select a Filter**:
    - Choose the desired filter from the "Select Filter" dropdown.
3. **Apply the Filter**:
    - Click the "Apply" button to process the image with the selected filter.
4. **View Results**:
    - Compare the original and processed images in the "Before" and "After" canvases.
    - View the histogram for further analysis.
5. **Save the Processed Image**:
    - Use the "Save" button to export the processed image.
6. **Reset (if needed)**:
    - Click the "Reset" button to start over.
    - Delete histogram from your device.

---

## Additional Notes

- Ensure that the required Python packages are installed:
    
    ```bash
    pip install numpy==1.21.0 pillow opencv-python matplotlib==3.4.3 scikit-image
    ```
    
- Periodic noise filtering requires specifying a direction or type.
- The application supports both grayscale and color images.
