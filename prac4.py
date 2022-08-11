new_list = []
a = int(input("Enter number of elements : "))
for i in range(a):
    new_list.append(int(input()))
print(new_list)
b = int(input("Enter element to be inserted"))
c = int(input("Position : "))
new_list.insert(c,b)
print(new_list)
b = int(input("Enter element to be deleted"))
new_list.remove(b)
print(new_list)
mylist = new_list.copy()
print("List is copied sucessfully")
del new_list
print(mylist[1:3])
b = int(input("Enter element to be searched"))
c = 0
for i in range(len(mylist)):
    if mylist[i] == b:
        c = 1
if c == 0:
    print("Element not found")
else:
    print("Element found")
another_list = [1,4,6]
list3= another_list+mylist
print(list3)
print("List after extending ",another_list.extend(mylist))
