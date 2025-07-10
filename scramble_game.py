import random

word_list = [
    "python", "developer", "programming", "algorithm", "function", "variable",
    "debugging", "compiler", "codechef", "machine", "bitcoin", "operation"
]

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def guess_word(original_word):
    attempts = 3
    while attempts > 0:
        guess = input("Guess the word (or type 'exit' to quit): ").lower()
        if guess == "exit":
            print(f"The correct word was: {original_word}\n")
            print("Thanks for playing! Goodbye!")
            return "exit"
        if guess == original_word:
            print("Correct! You guessed it!\n")
            return
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")
    print(f"The correct word was: {original_word}\n")

def play_game():
    while True:
        original_word = random.choice(word_list)
        scrambled = scramble_word(original_word)
        print("\nWelcome to the Word Scramble Game!")
        print(f"Scrambled word: {scrambled}")
        if guess_word(original_word) == "exit":
            break
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
