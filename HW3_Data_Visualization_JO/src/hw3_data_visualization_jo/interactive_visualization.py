import sys
import os

# Ensure the 'src' directory is added to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, '../../../HW3_Data_Visualization_JO/src'))
sys.path.insert(0, src_path)  # Insert at the beginning to prioritize

# Debugging: Print out the current sys.path to verify if 'src' is properly added
print("Updated sys.path:", sys.path)

import panel as pn
import matplotlib.pyplot as plt

try:
    from hw3_data_visualization_jo.data_loader import DataLoader  # Import DataLoader
except ImportError as e:
    print(f"Import Error: {e}")

# Load the Panel extension
pn.extension()

# Load images and labels
data_loader = DataLoader(r"C:\Users\jobri\OneDrive - Drexel University\MEM679\cropped_cards_data")
images, labels = data_loader.load_images()

# Interactive Visualization using Panel
def display_image_selector(images, labels):
    """Panel interface to select and view individual images."""
    def view_image(idx):
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
