import pandas as pd
import numpy as np

def generate_prediction():
    """Generate a mock prediction based on a sample dataset."""
    # Load sample data
    data = pd.read_csv('data_sample.csv')
    
    # Perform simple statistical operations
    mean_value = np.mean(data['Value'])
    max_value = np.max(data['Value'])
    
    # Mock prediction logic
    prediction = {
        'mean_inventory': mean_value,
        'max_inventory': max_value,
        'recommendation': 'Increase stock' if mean_value < 50 else 'Stock is sufficient'
    }
    
    return prediction
