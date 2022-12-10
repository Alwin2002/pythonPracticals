import pandas as pd
raw= {'first-name':['rupali','kunal','atul'],'last-name':['dhotre','mehta','mishra']}
df= pd.DataFrame(raw)
print(df)


c = pd.Series([1,2, 3, 5, 2],dtype='category')
print (c)

d=c.cat.rename_categories([9,8,7,6])
print(d) 