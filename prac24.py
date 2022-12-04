import numpy as np
Numbers = np.array([-36,0,51,-2,-8,0,-6,66,91,0,0,-7])
positive=[]
negative=[]
zeros=[]
for i in Numbers:
    if i==0:
        zeros.append(i)
    elif i>0:
        positive.append(i)
    else:
        negative.append(i)
print('Zero in array: ',zeros)
print('Positive elements in array: ',positive)
print('Negative elements in array: ',negative)