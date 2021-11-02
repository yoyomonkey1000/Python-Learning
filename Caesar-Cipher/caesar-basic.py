# Caesar Cypher Basic Version from PCAP
# This version only has a key of 1 and used the Ord and Chr string methods.
# The Program will be improved overtime
# By Jazz Arshad

orig_message = "Hello World"
encr_message = ""


def key1_encrypter(original_message): # this will shift the characters by 1 in the ascii chain

    original_message = original_message.lower() #turn all chars into lowercase
    encrypted_message= ""

    for char in original_message: # for every char in the lower message
        if char == 'z': # if its a z jus cycle it round to a
            encrypted_message += 'a'
        elif char == ' ': # if its a space leave it as a space
            encrypted_message += ' '
        else:  # if its any other character 
            encrypted_message += (chr(ord(char)+1))
    return encrypted_message
    


encr_message = key1_encrypter(orig_message)
print(orig_message, "will be encrypted to", encr_message)