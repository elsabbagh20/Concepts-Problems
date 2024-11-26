import random 

def scrambleWord (word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)


def wordScrambled (words):
        theOriginalWord = random.choice(words)
        scrambledWord = scrambleWord(theOriginalWord)

        print("Welcome to the word Scramble Game!")
        print("Try to Guess The Original Word from the scrambled Word", scrambledWord)
        print("You have 5 attempts.")


        attempts = 5
        while attempts > 0 :
            guess =  input("Enter Your Guess: ").strip()
            if not guess :
                print("Invalid input! Please Enter a word.")
                
                continue

            if guess == theOriginalWord:
                print ("Congratulation! You guessed the correct word.!")
                return
            attempts -=1
            print("Incorrect! Try again . You have", attempts, "attempts")
        print("You Are out of attempts! The Correct Word was: ", theOriginalWord )





wordsList = ["apple", "banana", "cocunut", "date", "cherry"]
wordScrambled(wordsList)