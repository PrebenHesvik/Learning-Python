import pytest
import pandas as pd
import numpy as np

rands = np.random.rand(6, 3) * 100
df = pd.DataFrame(rands, columns=[f'col_{i.upper()}' for i in 'abc'])

def is_dataframe(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError('You must provide a DataFrame')
    

# ------- TESTS ---------
def test_is_dataframe():
    df = [1, 2, 3]
    with pytest.raises(TypeError):
        is_dataframe(df)
        
