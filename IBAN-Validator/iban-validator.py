# This is an iban validator
#


def iban_validator(iban_number):
    iban_number = iban_number.replace(" ", "") # replace the spaces with no space

    #checks for invalid iban with any character which is not alpha or num
    if not iban_number.isalnum():
        print("This is not an IBAN ")
    elif len(iban_number) < 15: # check if the IBAN has atleast 15 chars
        print("The number is too short to be an IBAN")
    elif len(iban_number) > 31: #check if IBAN is more than 31 character
        print("The number is too long to be an IBAN")
    else: # so if it get past all the above errors its a IBAN candidate.
        print(iban_number[4:]) # print from the 5 character onwards
        print(iban_number[:4]) # print first 4 chars
        print(iban_number[4:] + iban_number[:4].upper()) #shows when you move the first 4 chars to the end and concatenate and upper
        iban_number = (iban_number[4:] + iban_number[0:4]).upper() #take the first 4 chars and concatenate at the end and turn all letters to upper case.
        
        #now that iban is in the correct format when can now process it
        # 
        iban_number2 = ''
        for character in iban_number:
            if character.isdigit():
                iban_number2 += character
            else: #turn the char into a ascii number and do a calc 
                iban_number2 += str(10 + ord(character) - ord('A'))
        iban_number2 = int(iban_number2)
        if iban_number2 % 97 == 1:
            print("IBAN is valid")
        else:
            print("IBAN is invalid")


def main():
    iban_num=input("Please enter in the IBAN number to validate: ")
    iban_validator(iban_num)


if __name__ == "__main__":
    main()
  
