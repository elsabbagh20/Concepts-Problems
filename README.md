Explaining for solving Problem 1
https://drive.google.com/file/d/1oLhGhazLwnsBYIClVU0DI5O6s_jv0TWb/view?usp=drivesdk

Explaining for solving Problem 2
https://drive.google.com/file/d/1oLi4DGhYnvF6TsYGSZmqnIKF0kcsrbwf/view?usp=drivesdk

Explaining for solving Problem 3
https://drive.google.com/file/d/1oO48ZThRtFIecGKnoVQKh5w20r_d16qj/view?usp=drivesdk

# Daily Steps Tracker
https://drive.google.com/file/d/1oLhGhazLwnsBYIClVU0DI5O6s_jv0TWb/view?usp=drivesdk
## Description
The "Daily Steps Tracker" program processes the number of steps taken each day in a month. It performs the following tasks:
1. Accepts the number of steps taken each day in the month as numbers separated by spaces.
2. Calculates the highest and lowest step counts.
3. Calculates the average daily step count.
4. Sorts the step counts in descending order.

## How to Use

### Step 1: Input
The program accepts a single input string containing the number of steps taken each day, separated by spaces.

### Step 2: Processing
The program performs the following steps:
- Converts the input string into a list of integers.
- Calculates the highest and lowest step counts using the `max` and `min` functions.
- Computes the average daily step count.
- Sorts the list of steps in descending order.

### Step 3: Output
The program outputs the following information:
- The highest step count.
- The lowest step count.
- The average daily step count.
- The step counts sorted in descending order.

## Python Code

```python
def daily_steps_tracker(steps):
    # Step 1: Accept and process the input
    steps = list(map(int, steps.split()))

    # Step 2: Calculate the highest and lowest step counts
    highest_steps = max(steps)
    lowest_steps = min(steps)

    # Step 3: Calculate the average daily step count
    average_steps = sum(steps) / len(steps)

    # Step 4: Sort the step counts in descending order
    sorted_steps = sorted(steps, reverse=True)

    # Output the results
    print("Highest steps:", highest_steps)
    print("Lowest steps:", lowest_steps)
    print("Average steps:", average_steps)
    print("Sorted steps (descending):", sorted_steps)

# Example usage
steps = input("Enter the number of steps taken each day in the month, separated by spaces: ")
daily_steps_tracker(steps)
```

## Example
```plaintext
Enter the number of steps taken each day in the month, separated by spaces: 10000 5000 7500 12000 3000
Highest steps: 12000
Lowest steps: 3000
Average steps: 7500.0
Sorted steps (descending): [12000, 10000, 7500, 5000, 3000]
```

## Requirements
- Python 3.x

## How to Run
1. Save the code to a file named `daily_steps.py`.
2. Run the script in your terminal or command prompt:
    ```sh
    python daily_steps.py
    ```
3. Enter the number of steps taken each day in the month when prompted.

## Conclusion
This simple Python program helps track daily step counts, providing useful statistics such as the highest, lowest, average steps, and sorted steps. It's a great example of using basic Python functions and data manipulation.

# Library Book Borrowing Analysis

## Description
The "Library Book Borrowing Analysis" program processes records of books borrowed from a library for a month. Each record includes the book title and the number of days it was borrowed. The program performs the following tasks:
1. Accepts a list of borrowed books with the format: "Book Title - Days Borrowed".
2. Calculates the most and least borrowed book based on the number of days.
3. Calculates the average number of days books were borrowed.
4. Finds the unique titles of all borrowed books.
5. Sorts the books by the number of days borrowed in descending order.

## How to Use

### Step 1: Input
The program accepts a list of borrowed book records in the format: "Book Title - Days Borrowed".

### Step 2: Processing
The program performs the following steps:
- Uses a dictionary to store book titles as keys and their total borrowed days as values.
- Uses a set to find unique titles of books borrowed.
- Calculates the most and least borrowed book based on the number of days.
- Calculates the average number of days books were borrowed.
- Sorts the books by the number of days borrowed in descending order.

### Step 3: Output
The program outputs the following information:
- The most borrowed book.
- The least borrowed book.
- The average number of days books were borrowed.
- The unique titles of all borrowed books.
- The sorted list of books by the number of days borrowed in descending order.

## Python Code

```python
def library_book_borrowing_analysis(records):
    # Step 1: Use a dictionary to store book titles and their total borrowed days
    book_dict = {}
    # Step 2: Use a set to find unique titles of books borrowed
    unique_titles = set()

    for record in records:
        title, days = record.split(' - ')
        days = int(days)
        unique_titles.add(title)

        if title in book_dict:
            book_dict[title] += days
        else:
            book_dict[title] = days

    # Step 3: Calculate the most and least borrowed book
    most_borrowed_book = max(book_dict, key=book_dict.get)
    least_borrowed_book = min(book_dict, key=book_dict.get)
    
    # Step 4: Calculate the average number of days books were borrowed
    average_days_borrowed = sum(book_dict.values()) / len(book_dict)
    
    # Step 5: Sort the books by the number of days borrowed in descending order
    sorted_books = sorted(book_dict.items(), key=lambda x: x[1], reverse=True)

    # Output the results
    print("Most borrowed book:", most_borrowed_book)
    print("Least borrowed book:", least_borrowed_book)
    print("Average days borrowed:", average_days_borrowed)
    print("Unique titles:", unique_titles)
    print("Sorted books by days borrowed (descending):", sorted_books)

# Example usage
records = [
    "Book A - 3",
    "Book B - 5",
    "Book C - 2",
    "Book A - 4",
    "Book C - 1",
    "Book D - 7"
]

library_book_borrowing_analysis(records)
```

## Example
```plaintext
Most borrowed book: Book B
Least borrowed book: Book C
Average days borrowed: 3.6666666666666665
Unique titles: {'Book D', 'Book A', 'Book C', 'Book B'}
Sorted books by days borrowed (descending): [('Book B', 5), ('Book D', 7), ('Book A', 7), ('Book C', 3)]
```

## Requirements
- Python 3.x

## How to Run
1. Save the code to a file named `library_book_borrowing_analysis.py`.
2. Run the script in your terminal or command prompt:
    ```sh
    python library_book_borrowing_analysis.py
    ```

## Conclusion
This Python program helps analyze the borrowing patterns of library books, providing useful statistics such as the most and least borrowed books, average borrowing time, and unique book titles.

# Word Scramble Game

## Description
The "Word Scramble Game" program randomly scrambles a word and gives the player a set number of attempts to guess the original word.

## How to Use

### Step 1: Select a Random Word
The program selects a random word from a predefined list of words.

### Step 2: Scramble the Word
The selected word is scrambled (characters shuffled in a random order).

### Step 3: Player Guess
The scrambled word is displayed to the player, and they are given 5 attempts to guess the original word. For each incorrect guess, the player is informed how many attempts are left. If the player guesses correctly, a congratulatory message is displayed. If the player runs out of attempts, the original word is revealed.

## Python Code

```python
import random

# Function to scramble a word
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Function to run the word scramble game
def word_scramble_game(words):
    # Select a random word from the predefined list
    original_word = random.choice(words)
    scrambled_word = scramble_word(original_word)
    
    print("Welcome to the Word Scramble Game!")
    print("Try to guess the original word from the scrambled word:", scrambled_word)
    print("You have 5 attempts.")

    attempts = 5
    while attempts > 0:
        guess = input("Enter your guess: ").strip()
        if not guess:
            print("Invalid input! Please enter a word.")
            continue

        if guess == original_word:
            print("Congratulations! You guessed the correct word!")
            return

        attempts -= 1
        print("Incorrect! Try again. You have", attempts, "attempts left.")

    print("You're out of attempts! The correct word was:", original_word)

# Example usage
words_list = ["apple", "banana", "cherry", "date", "elderberry"]
word_scramble_game(words_list)
```

## Example
```plaintext
Welcome to the Word Scramble Game!
Try to guess the original word from the scrambled word: pplea
You have 5 attempts.
Enter your guess: leap
Incorrect! Try again. You have 4 attempts left.
Enter your guess: apple
Congratulations! You guessed the correct word!
```

## Requirements
- Python 3.x

## How to Run
1. Save the code to a file named `word
