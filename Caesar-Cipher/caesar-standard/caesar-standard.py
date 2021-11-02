# caesar-standard is another attempt at doing the caesar cipher 
# which uses a symbol set and a key
# came from cracking codes with python

input_message = "Hello again"
decision = "d"
output_message = ""
SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
key = "2"

def get_input(original_message):
    return original_message


def caesar_engine(original_message):
    for char in original_message:
        print(char)



def main():
    print(get_input(input_message))
    caesar_engine(input_message)






main()