# caesar-standard is another attempt at doing the caesar cipher 
# which uses a symbol set and a key
# came from cracking codes with python

input_message = "Hello agai@!n"
decision = 'e'
output_message = ""
SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
key = 2

def get_input(original_message):
    return original_message


def caesar_engine(original_message):
    processed_message = ""
    processed_value = 0
    
    for char in original_message:
        if char not in SYMBOL:
            processed_message += char    
        elif decision == "e":
            processed_value = SYMBOL.index(char) + key
            if processed_value > len(SYMBOL):
                processed_value = SYMBOL[processed_value] - len(SYMBOL)
            processed_message += SYMBOL[processed_value]
        elif decision == 'd':
            processed_value = SYMBOL.index(char) - key
            if processed_value < 0:
                processed_value = SYMBOL[processed_value] + len(SYMBOL)
            processed_message += SYMBOL[processed_value]
        else:
            print("You have entered invalid input")

    return(processed_message)




def main():
    print(get_input(input_message))
    print(caesar_engine(input_message))






main()