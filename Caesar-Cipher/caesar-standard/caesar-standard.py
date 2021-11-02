# caesar-standard is another attempt at doing the caesar cipher 
# which uses a symbol set and a key
# came from cracking codes with python

SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

input_message = input("Please enter in string here : ")
decision = input("Would you like to (e)ncrypt or (d)ecrypt? ")
key = int(input("Please enter in key number : "))
output_message = ""

def get_input(original_message):
    return original_message


def caesar_engine(original_message):
    processed_message = ""
    processed_value = 0
    
    for char in original_message:
        if char not in SYMBOL:
            processed_message += char
            continue   
        elif decision == "e":
            processed_value = SYMBOL.index(char) + key
            if processed_value > len(SYMBOL)-1:
                processed_value = processed_value - len(SYMBOL)
        elif decision == 'd':
            processed_value = SYMBOL.index(char) - key
            if processed_value < 0:
                processed_value = processed_value + len(SYMBOL)
        processed_message += SYMBOL[processed_value]
    

    return(processed_message)


def main():
    print(get_input(input_message))
    print(caesar_engine(input_message))



main()