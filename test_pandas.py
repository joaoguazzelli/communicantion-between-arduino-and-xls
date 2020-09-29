import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.DataFrame({'1':[1,3,5,7,4,5,6,4,7,8,9],
                   '1':[3,5,6,2,4,6,7,8,7,8,9]})

writer = ExcelWriter('Pandas-Example2.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()