# word-checker 
# takes 2 inputs and tells you if the second word exists in the first.


def word_finder(word_one, word_two):
    if word_one.find(word_two) != -1:
        print(f"{word_two} is in {word_one}")
    else:
        print(f"{word_two} is not in {word_one}")

#inputs
first_word=(input("Please type in your word that you want to search: ").lower())
second_word = (input("Please type in the word you are searching for: ").lower())

#use the function 
word_finder(first_word,second_word)