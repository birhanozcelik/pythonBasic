userInput = int(input("please enter the number: "))
count = 1

while count != userInput:
    if (userInput % count) == 0:
        print(count)
        count += 1
    else:
        count += 1