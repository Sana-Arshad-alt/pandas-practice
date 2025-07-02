import pandas as pd
s = pd.Series([1,2,3,4])
print(s)
#%%
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.mean())
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.value_counts())
print(s.head(3))
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.tail())
#%%
import pandas as pd
s = pd.Series([35,45,55,65,45,35,55,25,45])
print(s.size)
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.shape)
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.dtype)
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.sum())
print(s.mean())
print(s.median())
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.values)
print(s.index)
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.max())
print(s.min())
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.std())
print(s.describe())
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
s.sort_values(ascending=False)
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.sort_index())
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.astype(float))
#%%
import pandas as pd
s=pd.Series([35,45,55,65,45,35,55,25,45])
print(s.duplicated())
