# improved Caesar Cipher Exercise in the PCAP
# Leeps letters case 
# Do the ASCII ORD conversion + key 

orig_message = "Hello World"
out_message = ""
choice = "e"
key = 20



def caesar_engine(original_message, choice):
    output_message=""
    char =""

    if choice == 'e':
        for character in original_message:
            if character.isalpha():
                char = ord(character)  + key
            else:
                output_message += character
                continue 
            if character.isupper():
                if char > ord('Z'):
                    char = char - 26
            elif character.islower():
                if char > ord('z'):
                    char = char -26
            output_message += chr(char)
    elif choice == 'd':
        for character in original_message:
            if character.isalpha():
                char = ord(character) - key
            else:
                output_message += character
                continue
            if character.isupper():
                if char < ord('A'):
                    char = char + 26
            elif character.islower():
                if char < ord('a'):
                    char = char + 26
            output_message += chr(char)
    return output_message


print(orig_message)
out_message = (caesar_engine(orig_message, 'e'))
print(out_message)
out_message = (caesar_engine(out_message, 'd'))
print(out_message)