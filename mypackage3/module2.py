"""Module that requires pandas to be installed"""

import pandas as pd

def func_requiring_pandas(
    array_x:list,
    array_y:list
    ) -> pd.DataFrame:
    """Returns pandas dataframe from 2 input arrays

    Args:
        array_x (list): _description_
        array_y (list): _description_
    
    Returns:
        pd.DataFrame: _description_
    """
    df = pd.DataFrame({
        "array_x":array_x,
        "array_y":array_y
        }, index=range(len(array_x)))

    return df
