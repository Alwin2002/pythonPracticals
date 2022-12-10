data = open('testing.txt').read()

print('Reading the whole file :',data)

#reading data with btyes defined 

data1 = open('testing.txt').read(3)
print('Reading only three 3 bytes: ',data1)

#reading data with readline method

data2=open('testing.txt').readlines()
print('Reading lines with readline method:',data2)