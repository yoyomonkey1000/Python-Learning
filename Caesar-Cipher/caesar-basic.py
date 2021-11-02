# Caesar Cypher Basic Version from PCAP
# This version only has a key of 1 and used the Ord and Chr string methods.
# The Program will be improved overtime
# By Jazz Arshad

original_message = "Hello World"
encrypted_message = ""

original_message = original_message.lower()

for char in original_message:
    if char == 'z':
        encrypted_message += 'a'
    elif char == ' ':
        encrypted_message += ' '
    else:
        encrypted_message += (chr(ord(char)+1))




print(original_message, "will be encrypted to", encrypted_message)