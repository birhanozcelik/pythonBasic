a = [1,2,5,9,8,7,3,0,15,265,25,45,98,2,6,4,30,4]
count = 0
for x in range(len(a)):
    if a[x] < 5:
        count+=1
        print(a[x])
print(count)



