# palindrome detector
# This will take a string remove any spaces, 
# turn to lowercase, checks is the first and 
# last letter the same and works its way in. 

inp_message = "Go hang a salami, I’m a lasagna hog."
#inp_message = (input("Please enter in your string: "))


def palindrome_engine(input_message): 

    input_message = (input_message.lower()).replace(' ','') # strip out spaces from string
    preprocessed_message =""
    i = 0 # set i to go up string to 0
    x = -1 # set x to -1 which is last character of a string
     
    # THIS DOESNT WORK input_message = (input_message.translate(str.maketrans('', '', string.punctuation()))) # from the import string package  
    
    for char in input_message: # go through every char in the string 
        if  not char.isalnum(): # if the character is alpha numeric write it in
            continue
        else:
            preprocessed_message += char 
    print(preprocessed_message, " given to engine")
    print(int(len(preprocessed_message)/2)) # see if te string can be split properly
    while i <= (int(len(preprocessed_message)/2)):
        print(preprocessed_message[i] ," compared with " , preprocessed_message[x])
        if (preprocessed_message[i]) != (preprocessed_message[x]): # if the strings dont match just return false
            return False
        else: 
            i += 1 # increment i to the next index in the string
            x -= 1 # decrement x to the prceeding index in the string
    return True


if palindrome_engine(inp_message):
    print(f"The string {inp_message} is a palindrome")
else:
    print(f"The string {inp_message} is not a palidrome")

