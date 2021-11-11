#more revisors from PCAP 
weird_phrase = "Silly walk"

for letter in weird_phrase:
    print(letter, end = ' ')

print()  

#can also write the above 

for letter in range(len(weird_phrase)):
    print(weird_phrase[letter], end = " " ,sep = " ")

print()

#slices example the bottom ones show the jumping

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


# in and not in checkers

alphabet = " abcdefghiklmnnop" # strings are immutable so no append or del or insert but can be concatenated

print('f' in alphabet)
print('F' in alphabet)
print ('1' in alphabet)
print('ghi' in alphabet)

#not in now 

print('f' not in alphabet)
print('F' not in alphabet)
print ('1' not in alphabet)
print('ghi' not in alphabet)

# min 
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


print(max("ABCDEFGHIZabcdefxy"))

print(max([0,1,2,777]))

print([0,1,20,777].index(20))

print(list("123456"))

print(("123435262").count("2"))


print("abcdefGHIkkl".capitalize()) # sorts out all characthers and capitalises the first

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# Demonstrating the find() method: same as index but safer!!
print("Eta".find("ta"))
print("Eta".find("mma"))

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())


# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

print("pythoninstitute.org".lstrip(".org"))
print("pythoninstitute.org".strip(".org"))
print("pythoninstitute.org".rstrip(".org"))

print("This is it!".replace("is", "are", 1))
print("This is it is is is was is !".replace("is", "are", 3))


# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demonstrating the split() method: split string into list
print("phi       chi\npsi".split())
# opposite is join
print(" ".join(["phi", "chi" , "psi"])) # need to create something to join it too.


# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")


#changing strings

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()


# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())


#d two replaces
s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)




# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


