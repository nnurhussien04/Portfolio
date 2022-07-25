word = "Hello"
letters = list(word)
right = []
lives = 5
while True:
    guess = input("Guess a letter")
    if guess in word.lower() or guess in word.upper():
        try:
            if word.count(guess) > 1:
                for x in range(word.count(guess)):
                    index = letters.index(guess,x+1)
                    right.insert(index, guess)
            else:
                index = letters.index(guess)
                right.insert(index,guess)
                print(index)
        except :
            try:
                index = letters.index(guess)
                right.insert(index,guess)
            except :
                    print('Error')
        print("Right:", right)
    else:
        lives -= 1
        print(f"Here is the lives remaning {lives}")

    if (len(right) == len(letters) or len(right) < len(letters)):
        if letters == right:
            print(len(right),len(letters))
            print("You got the word")
            break
        else:
            print(letters)

    if lives == 0:
        print(f'You lost, the word was {word}')
        break
