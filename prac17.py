import numpy as np
a = np.array(['Java','Python','C','Java'])
a = np.char.encode(a, encoding='cp037')
print("Encoded array",a)
a = np.char.decode(a, encoding='cp037')
print("Decoded array",a)