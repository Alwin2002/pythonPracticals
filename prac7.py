set1 = {1,2,3,4}
a = int(input("Enter element to be searched"))
if a in set1:
    print("Element found")
else:
    print("Element not found")
a = int(input("Enter element to be inserted :"))
set1.add(a)
print(set1)
a = int(input("How many elements to be inserted :"))
for i in range(a):
    set1.add(int(input()))
print(set1)
print("Length of set is",len(set1))
a = int(input("Enter element to be deleted :"))
set1.discard(a)
print(set1)
set2 = {5,6,7}
set3 = set1.union(set2)
print(set3)
del set3
print("Set3 deleted")