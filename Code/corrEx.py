import pandas as pd
df = pd.DataFrame({'A': range(4), 'B': [2*i for i in range(4)]})

   A  B
0  0  0
1  1  2
2  2  4
3  3  6


df['A'].corr(df['B'])
df.loc[2, 'B'] = 4.5
df['A'].corr(df['B'])
df.corr()
     
