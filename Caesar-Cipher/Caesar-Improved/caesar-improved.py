# improved Caesar Cipher Exercise in the PCAP
# Leeps letters case 
# Do the ASCII ORD conversion + key 

orig_message = "Hello World"
out_message = ""
key = 20
char = ""

for character in orig_message:
    if character.isalpha():
        char = ord(character)  + key
    else:
        out_message += character
        continue
    
    if character.isupper():
        char = ord(character)  + key
        if char > ord('Z'):
            char = char - 26
    elif character.islower():
        if char > ord('z'):
            char = char -26
    out_message += chr(char)

print(out_message)