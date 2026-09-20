import random

words = ["python", "computer", "school", "banana", "developer"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0

while wrong_guesses < 6:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display = display + letter
        else:
            display = display + "_"

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses = wrong_guesses + 1
        print("❌ Wrong!")
        print("Wrong guesses:", wrong_guesses)

if wrong_guesses == 6:
    print("\n💀 Game Over!")
    print("The word was:", word)
