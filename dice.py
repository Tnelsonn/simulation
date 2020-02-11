
someInt = float(input("roll times: "))
print("You entered : " + str(someInt))
print(f"You entered : {someInt}")

import random
roll = random.randint(1,6)


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

i=0
while(i < someInt):
    roll = random.randint(1,6)
    print (roll)
    i+= 1


    if (someInt == 1):
        one+= 1
        print(one/someInt)
    if(someInt == 2):
        two+= 1
        print(two/someInt)
    if(someInt == 3):
        three+= 1
        print(three/someInt)
    if(someInt == 4):
        four+= 1
        print(four/someInt)
    if(someInt == 5):
        five+= 1
        print(five/someInt)
    if(someInt == 6):
        six+= 1
        print(six/someInt)
        



