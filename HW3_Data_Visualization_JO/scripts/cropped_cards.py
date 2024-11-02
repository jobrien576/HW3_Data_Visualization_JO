import os
import cv2
import numpy as np
from PIL import Image
import pillow_heif

# Register HEIF with Pillow
pillow_heif.register_heif_opener()

# Define the input and output directories
input_dir = "C:/Users/jobri/OneDrive - Drexel University/MEM679/cards_data/"
output_dir = "C:/Users/jobri/OneDrive - Drexel University/MEM679/cropped_cards_data/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Increase padding around the detected bounding box
padding = 20  # Adjusted padding

# Minimum area for a contour to be considered as the card
min_area = 5000  # This may need adjustment based on image resolution

# Walk through all subdirectories and files in the input directory
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(".HEIC"):  # Adjust for .HEIC format
            # Construct full file path
            file_path = os.path.join(root, filename)
            print(f"Processing file: {file_path}")

            # Open the HEIC file with pillow_heif
            image = Image.open(file_path)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convert PIL to OpenCV format

            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Compute median pixel intensity to set adaptive Canny thresholds
            median_intensity = np.median(gray)
            lower_thresh = int(max(0, 0.66 * median_intensity))
            upper_thresh = int(min(255, 1.33 * median_intensity))

            # Use adaptive Canny edge detection
            edges = cv2.Canny(gray, lower_thresh, upper_thresh)

            # Dilate edges to capture the full card outline
            kernel = np.ones((5, 5), np.uint8)
            dilated_edges = cv2.dilate(edges, kernel, iterations=1)

            # Find contours from the dilated edges
            contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Filter contours by area and find the largest valid contour
            valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
            if valid_contours:
                largest_contour = max(valid_contours, key=cv2.contourArea)
                rect = cv2.minAreaRect(largest_contour)
                box = cv2.boxPoints(rect)
                box = np.int32(box)  # Ensure coordinates are integers

                # Calculate the width and height of the rotated rectangle
                width = int(rect[1][0])
                height = int(rect[1][1])

                # Create a perspective transformation matrix to rotate and crop the card
                src_pts = box.astype("float32")
                dst_pts = np.array([[0, height-1],
                                    [0, 0],
                                    [width-1, 0],
                                    [width-1, height-1]], dtype="float32")
                M = cv2.getPerspectiveTransform(src_pts, dst_pts)
                warped = cv2.warpPerspective(image, M, (width, height))

                # Apply increased padding around the cropped card
                padded_image = cv2.copyMakeBorder(warped, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])

                # Determine the relative folder structure in the output directory
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)

                # Ensure the output subdirectory exists
                os.makedirs(output_subdir, exist_ok=True)

                # Save the cropped image with padding to the output directory as JPEG
                output_path = os.path.join(output_subdir, filename.replace(".HEIC", ".jpg"))
                cv2.imwrite(output_path, padded_image)
                print(f"Cropped and saved {filename} to {output_path}")
            else:
                print(f"No valid contours found for {filename}, skipping.")
