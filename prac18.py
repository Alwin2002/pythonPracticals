import numpy as np
x = np.array(['2', '11', '234', '1234', '12345'])
print("\nOriginal Array:")
print(x)
r = np.char.zfill(x, 4)
print("\nNumeric string of 4 digits with zeros:")
print(r)


