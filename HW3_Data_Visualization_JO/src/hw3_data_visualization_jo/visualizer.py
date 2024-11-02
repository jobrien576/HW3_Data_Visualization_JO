import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    """A class for creating static visualizations of the dataset.

    Attributes:
        images (list): List of images in numpy array format.
        labels (list): List of labels associated with the images.
    """

    def __init__(self, images, labels):
        """
        Initializes the Visualizer with a set of images and labels.

        Args:
            images (list): List of numpy arrays representing images.
            labels (list): List of labels corresponding to each image.
        """
        self.images = images
        self.labels = labels

    def display_sample_images(self, num_samples=5):
        """
        Displays a random selection of images from the dataset.

        Args:
            num_samples (int): Number of images to display. Defaults to 5.
        """
        sample_indices = np.random.choice(len(self.images), num_samples, replace=False)
        plt.figure(figsize=(10, 5))
        for i, idx in enumerate(sample_indices, 1):
            plt.subplot(1, num_samples, i)
            plt.imshow(self.images[idx])
            plt.title(self.labels[idx])
            plt.axis("off")
        plt.show()
