import numpy as np
import pandas as pd

def generate_random_dataframe(rows=10):
    """
    Generate a DataFrame with two columns 'X' and 'Y' containing random numbers.
    :param rows: Number of rows to generate
    :return: A DataFrame with random data
    """
    data = {
        'X': np.random.rand(rows),
        'Y': np.random.rand(rows)
    }
    
    df = pd.DataFrame(data)
    return df
