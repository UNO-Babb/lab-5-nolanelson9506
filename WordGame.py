#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""

    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""

    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for i in range(len(myGuess)):
            letter = myGuess[i]
            if inSpot(letter, word, i):
                result += letter.upper()
            elif inWord(letter, word):
                result += letter.lower()
            else:
                result += "*"
    return result

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print("Attempt to guess the word in 6 tries!")

    #User should get 6 guesses to guess
    guesses = 6
    for attempt in range(guesses):
        guess = input(f"Guess {attempt+1}: ").lower()
        if len(guess) !=len(todayWord):
            print(f"Your word has to be {len(todayWord)} letters long.")
            continue
        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if guess == todayWord:
            print("Correct! You guessed the right word!")
            break
    else:
        print("You ran out of guesses! The word was:", todayWord)
    
    
  



if __name__ == '__main__':
  main()
