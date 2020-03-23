import pandas as pd
import numpy as np

def convertaition_df(columns: list, rows: list):
    """
    Convert report_date in type datetime and revenue in float.
    :param columns: list
    :param rows: array
    :return: DataFrame
    """
    df = pd.DataFrame(np.array(rows), columns=columns)
    df['report_date'] = pd.to_datetime(df['report_date'])
    df['revenue'] = df['revenue'].apply(lambda x: x.replace(',', '.'))
    df['revenue'] = df['revenue'].astype(float)
    return df

# convertaition_df(columns=['row_num', 'report_date', 'revenue'],
#                 rows=[[1, '2020-01-15', '1101,12'], [2, '2020-01-16', '22,10']]).info()