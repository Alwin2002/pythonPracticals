import numpy as np
import pandas as pd
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df=pd.DataFrame(dict)
print(df)
df=df.isnull()
print(df)