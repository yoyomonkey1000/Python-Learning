# Anagram checker
# get two strings and then see if they are anagrams  of each other


def anagram_finder(word_one, word_two):
    word_one = word_one.replace(' ','').split()
    word_two = word_two.replace(' ','').split()

    if (len(word_one)) != (len(word_two)) or word_one == word_two:
        print("NOT ANAGRAM ")
    
    word_one = word_one.sort()
    word_two = word_two.sort()
    print (word_one)
    print (word_two)

    i = 0
    while i < len(word_one):
        if word_one[i] == word_two[i]:
            print(f"{word_two} is an anagram of {word_one}")
            i += 1
        else:
            return False
    return True
    
        

#inputs
first_word=(input("Please type in your word that you want to search: ").lower())
second_word = (input("Please type in the word you are searching for: ").lower())

#use the function 
anagram_finder(first_word,second_word)