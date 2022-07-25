import random
##print('The Number Game')
##Game = int(input('Enter a Number '))
##num1 = random.randint(0,10)
##Game2 = Game-num1
##Game3 = num1 - Game
##if Game >= 0 and Game <=13:
##    if Game2 == 3 or Game3 == 3:
##        print('You are close and was 3 off')
##    elif Game2 == 2 or Game3 == 2:
##        print('You are very close and was 2 off')
##    elif Game2 == 1 or Game3 == 1:
##        print('You are not far away and was 1 off')
##    elif Game2 == 0 or Game3 == 0:
##        print('You are correct')
##    else:
##        print('You are incorrect the number was',num1)
##else:
##    print('You are incorrect the number  you inputted was far off, the number was',num1)

No = input('Enter Number')
RandomNumber = random.randint(0,100)
while No.isdigit() == False:
    print('This input is not a digit')
    No = input('Enter Number')
    if No.isdigit() == True:
        break

x = int(No)
while True:
    if x < 0:
        print('Its not in range')
        No = input('Enter Number')
        x = int(No)
    elif x > 100:
        print('Its not in range')
        No = input('Enter Number')
        x = int(No)
    else:
        if No == RandomNumber:
            print("Correct")
        else:
            print("Incorrect")
        print(RandomNumber)
        break

