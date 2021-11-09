# Caesar Cypher Basic Version from PCAP
# This version only has a key of 1 and used the Ord and Chr string methods.
# The Program will be improved overtime
# By Jazz Arshad


def key1_encrypter(original_message): # this will shift the characters by 1 in the ascii chain

    original_message = original_message.lower() #turn all chars into lowercase
    encrypted_message= ''

    for char in original_message: # for every char in the message
        if not char.isalpha(): #if the char is not a letter 
            encrypted_message += char # put it in as is
        elif char == 'z': # if its 'z' just cycle it round to a
            encrypted_message += 'a' #
        else:  # if its any other character 
            encrypted_message += (chr(ord(char)+1))
    return encrypted_message


def key1_decrypter(encrypted_message):

    encrypted_message = encrypted_message.lower()
    decrypted_message = '' 

    for char in encrypted_message:
        if not char.isalpha():
            decrypted_message += char
        elif char == 'a':
            decrypted_message += 'z'
        else:
            decrypted_message += (chr((ord(char))-1))
    
    return decrypted_message


def main():
    input_message = input("Please enter your message : \n ")
    decision = input("Would you like to encrypt(e) or decrypt(d)?: ")
    output_message = ""

    if decision == "e":
        output_message = key1_encrypter(input_message)
    elif decision == "d":
        output_message = key1_decrypter(input_message)
    
    print(f"{input_message} will be changed to {output_message}")

if __name__ == "__main__":
    main()