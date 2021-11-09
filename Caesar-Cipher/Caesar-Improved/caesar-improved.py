# improved Caesar Cipher Exercise in the PCAP
# Leeps letters case 
# Do the ASCII ORD conversion + key 


def caesar_engine(original_message, choice, key):
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


def main():
    orig_message = "Hello World"
    out_message = ""
    choice = "e"
    key = 20
    print(orig_message)
    out_message = (caesar_engine(orig_message, 'e', key))
    print(out_message)
    reverse_message = (caesar_engine(out_message, 'd', key))
    print(reverse_message)

if __name__ == "__main__":
    main()