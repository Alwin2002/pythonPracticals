
tuple1 = (2,3,4,5,6,2)
print("Length of tuple : ",len(tuple1))
print("Enter interval of slicing")
a = int(input())
b = int(input())
print("Sliced tuple : ",tuple1[a:b])
tuple2 = (12,23,45)
tuple3 = tuple1+tuple2
print(tuple3)
del tuple3
print("Tuple 3 deleted sucessfully")
list1 = [1,2,3,4]
print("List ",list1,"converted to tuple",tuple(list1))
