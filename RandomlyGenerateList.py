import random

list1 = []
list2 = []
list3 = []
random1 = random.randint(1,11)
random2 = random.randint(1,11)

for elm in range(random1):
    list1.append(random.randint(1,21))
print(list1)

for elm in range(random2):
    list2.append(random.randint(1,21))
print(list2)

for elm in range(random1):
   for elk in range(random2):
       if list1[elm] == list2[elk]:
           list3.append(list1[elm])
       else:
           continue
print(list3)





