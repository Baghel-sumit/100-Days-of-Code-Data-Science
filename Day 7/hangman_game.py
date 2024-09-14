import random

print("Welcome to hangman game!!!")

word_list = [ "camel", "baboon", "camel" ]

# TODO 1: Randomly choose a word from the word list and assign it to a variable called chosen_word. then print it.

chosen_word = random.choice(word_list)
final_answer = ''.join(['_ '] * len(chosen_word))

print("Your answer will be: ", final_answer)

# TODO 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Enter your guess: ").lower()

# TODO 3: Check if the letter user guessed is one of the letters in chosen_word. Print filled letter in final_answer

isCorrectGuess = False

for index in range(0, len(chosen_word)):
    letter = chosen_word[index]
    if (letter == guess):
        isCorrectGuess = True
        final_answer = final_answer[:index] + guess + final_answer[index + 1:]

print("Your replaced answer: ", final_answer)
    

