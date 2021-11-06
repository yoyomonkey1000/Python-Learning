# Anagram checker
# get two strings and then see if they are anagrams  of each other


from typing import cast


def anagram_checker(word_one, word_two):

    if word_one == word_two:
        print("The word is exactly the same")
    elif len((word_one)) == len((word_two)):
        if ((sorted(word_one)) == (sorted(word_two))):
            print(f"{word_one} and {word_two} are anagrams")
            return True
        else:
            print(f"{word_one} and {word_two} are not anagrams")
            return False
        

#inputs
first_word=(input("Please type in your word that you want to search: ").lower())
second_word = (input("Please type in the word you are searching for: ").lower())

#use the function 
if anagram_checker(first_word,second_word):
    print("Anagram")
else:
    print("Not Anagram")
