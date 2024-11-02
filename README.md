# HW3 Data Visualization Project

## Overview

This project is part of an assignment to create effective and engaging data visualizations for a custom dataset of playing card images. The project uses both static and interactive visualizations to help understand the dataset.

### Tools and Technologies Used
- **Python**
- **matplotlib** for static visualizations
- **Panel** for interactive visualizations
- **Pillow** for image handling

## Project Structure

- **src/hw3_data_visualization_jo/data_loader.py**: Contains the `DataLoader` class used to load and preprocess images from the dataset.
- **src/hw3_data_visualization_jo/visualizer.py**: Contains the static visualization code for the dataset.
- **src/hw3_data_visualization_jo/interactive_visualization.py**: Implements the interactive visualization using Panel.
- **tests/**: Contains unit tests for the different modules of the project.
- **HW3_Data_Visualization.ipynb**: A Jupyter notebook with static visualizations to explore the dataset.

## Getting Started

### Prerequisites
- **Python 3.8 or above**
- **Conda or Virtualenv** (for managing dependencies)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd HW3_Data_Visualization_JO
   ```

3. Create a virtual environment and activate it:
   ```bash
   conda create -n data_vis python=3.8
   conda activate data_vis
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Interactive Visualization
To view the interactive visualization:
1. Navigate to the project directory.
2. Run the following command:
   ```bash
   panel serve HW3_Data_Visualization_JO/src/hw3_data_visualization_jo/interactive_visualization.py --dev
   ```
3. Open the URL provided by the command output in your browser.

## Static Visualizations
Static visualizations are available in the Jupyter notebook `HW3_Data_Visualization.ipynb`. The notebook includes:
- Bar charts to visualize the number of images per rank and suit.
- A pie chart to show the distribution of suits. (LOL)

### Utility Scripts

The `scripts` folder contains useful utility scripts for this project:

- **crop_cards.py**: Script used to crop images of playing cards for preprocessing the dataset.


