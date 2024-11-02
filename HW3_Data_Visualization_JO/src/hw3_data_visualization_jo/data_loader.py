import os
import numpy as np
from PIL import Image
import pillow_heif  # Import pillow-heif to support HEIC images

class DataLoader:
    """A class to load and preprocess images from a dataset.

    Attributes:
        dataset_path (str): The path to the dataset directory.
    """

    def __init__(self, dataset_path):
        """
        Initializes the DataLoader with a given dataset path.

        Args:
            dataset_path (str): Path to the dataset containing image folders.
        """
        self.dataset_path = dataset_path
    
    def load_images(self, target_size=(128, 128)):
        """
        Loads and resizes images from the dataset.

        Args:
            target_size (tuple): A tuple specifying the desired width and height of images.

        Returns:
            list: A list of numpy arrays representing the images.
            list: A list of labels associated with the images.
        """
        images, labels = [], []
        for folder_name in os.listdir(self.dataset_path):
            folder_path = os.path.join(self.dataset_path, folder_name)
            if os.path.isdir(folder_path):
                rank, suit = folder_name.split('_')
                for img_name in os.listdir(folder_path):
                    if img_name.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
                        img_path = os.path.join(folder_path, img_name)
                        try:
                            img = Image.open(img_path).resize(target_size)
                            images.append(np.array(img) / 255.0)  # Normalize pixel values
                            labels.append(f"{rank}_{suit}")
                        except Exception as e:
                            print(f"Could not open image {img_path}: {e}")
        return images, labels
