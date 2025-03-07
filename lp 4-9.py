import random


def main():
    secret = random.randint(1,21)
    print(secret , " (The number is printed here for testing purposes)")
    play = input("What is your guess? The secret number is between 1 and 20.")
    print(f"The secret number was {secret}")
    print(f"You guessed {play}")
    if int(play) == secret:
        print("You Win!")
    else:
        print("you lost...")

if __name__ == "__main__":
    main()
