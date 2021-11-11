# Caesar Breaker
# build up from caesar-standard to decrypt messages

message = " hello blah blah"
SYMBOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

decrypted_index= '0'
key = 10


def caesar_breaker():

    decrypted_message = ""
    if len(message) == 0:
        print("empty message")
    
    for char in message:
        if char in SYMBOL:
            char_index = SYMBOL.find(char)
            decrypted_index = char_index - key
            if decrypted_index < 0:
                decrypted_index = decrypted_index + (len(SYMBOL))
            elif decrypted_index > len(SYMBOL):
                decrypted_index = decrypted_index - (len(SYMBOL))
            decrypted_message += SYMBOL[decrypted_index]
    
    print(decrypted_message)
            
caesar_breaker()