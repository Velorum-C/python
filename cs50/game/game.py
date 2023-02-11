from random import randint

while True:
    level = input("Level: ")
    if level.isnumeric() is not True:
        continue
    level = int(level)
    if level <= 0:
        continue
    break

answer = randint(0, level)

while True:
    guess = input("Guess: ")
    if guess.isnumeric() is not True:
        continue
    guess = int(guess)
    if guess <= 0:
        continue
    if guess < answer:
        print("Too small!")
        continue
    elif guess > answer:
        print("Too large!")
        continue
    print("Just right!")
    exit()
