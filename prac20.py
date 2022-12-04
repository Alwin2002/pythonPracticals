import numpy as np
arr = np.array(['Python','C#','Java'])
print("The Given Array: ",arr)
file = open('array.txt','w')
file.write(f'{arr}')
file.close
file = open("array.txt")
print(file.read())
file.close()



