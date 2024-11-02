import sys
import os
import panel as pn
import matplotlib.pyplot as plt
from hw3_data_visualization_jo.data_loader import DataLoader

# Load the Panel extension
pn.extension()

# Load images and labels
data_loader = DataLoader(r"C:\Users\jobri\OneDrive - Drexel University\MEM679\cropped_cards_data")
images, labels = data_loader.load_images()

def display_image_selector(images, labels):
    """
    Panel interface to select and view individual images.

    Args:
        images (list): List of numpy arrays representing images.
        labels (list): List of labels corresponding to each image.

    Returns:
        pn.interact: An interactive Panel widget for selecting and displaying images.
    """
    def view_image(idx):
        """
        Displays the selected image with its label.

        Args:
            idx (int): The index of the image to display.
        """
        plt.imshow(images[idx])
        plt.title(labels[idx])
        plt.axis("off")
        plt.show()

    return pn.interact(view_image, idx=(0, len(images) - 1))

# Serve the app
if __name__ == "__main__":
    component = display_image_selector(images, labels)
    pn.template.FastListTemplate(
        title="Playing Card Dataset Viewer",
        main=[component],
        accent="goldenrod"
    ).servable()
