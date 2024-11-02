# tests/test_data_loader.py
import pytest
from HW3_Data_Visualization_JO.data_loader import DataLoader

def test_create_labels_csv():
    loader = DataLoader("mock_path")
    loader.create_labels_csv("test_labels.csv")
    assert os.path.exists("test_labels.csv")  # Check if CSV is created
