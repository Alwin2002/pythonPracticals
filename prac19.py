import numpy as np
x = np.array(['cat', 'crocodile', 'anaconda', 'character'])
print("\nOriginal Array:",x)
r = np.char.count(x,'c')
print("Number of ‘c’:",r)



