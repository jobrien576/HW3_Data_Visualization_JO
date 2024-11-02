import os
import numpy as np
from PIL import Image
import pillow_heif  # Import pillow-heif to support HEIC images

class DataLoader:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
    
    def load_images(self, target_size=(128, 128)):
        """Loads and resizes images, returning them as numpy arrays."""
        images, labels = [], []
        for folder_name in os.listdir(self.dataset_path):
            folder_path = os.path.join(self.dataset_path, folder_name)
            if os.path.isdir(folder_path):
                rank, suit = folder_name.split('_')
                for img_name in os.listdir(folder_path):
                    # Only attempt to open files with supported image extensions
                    if img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
                        img_path = os.path.join(folder_path, img_name)
                        try:
                            img = Image.open(img_path).resize(target_size)
                            images.append(np.array(img) / 255.0)  # Normalize pixel values to 0-1
                            labels.append(f"{rank}_{suit}")
                        except Exception as e:
                            print(f"Could not open image {img_path}: {e}")
        return images, labels
