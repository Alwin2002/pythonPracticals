thisdict = { "brand": "Ford","model": "Mustang", "year": 1964 }
print(thisdict)
a = input("Enter key value to be changed : ")
b = input("Enter new value : ")
for i in thisdict:
  if i == a:
    thisdict[i] = b
print(thisdict)
for x,y in thisdict.items():
  print(x,y)
a = input("Enter key value to be searched : ")
if a in thisdict:
  print("Key value exists")
else:
  print("Key value do not exist")
print(len(thisdict))
thisdict["age"]=12
print(thisdict)
a = input("Enter key value to be deleted : ")
thisdict.pop(a)
print("Deleted")
thisdict.clear()
print(thisdict)

