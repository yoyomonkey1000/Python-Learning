# word-checker 
# takes 2 inputs and tells you if the second word exists in the first.


def word_finder (long_word, short_word):
    for char in short_word:
        print(long_word.find(char))
       # string_one.find(char)


def main():
    #inputs
    first_word=(input("Please type in your word that you want to search: ").lower())
    second_word = (input("Please type in the word you are searching for: ").lower())

    #use the function 
    word_finder(first_word,second_word)


if __name__ == "__main__":
    main()