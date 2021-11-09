# LED Numbers Display program
# Prints out the subsequent LED charater for a number
#

# Create a multi-dimensional  each character is a 5 row list and each list is 3 chars long
# There is 10 characters all in all 0-9
# Put this in a list called pattern. 

pattern = [ [['#','#','#'],
             ['#',' ','#'],
             ['#',' ','#'],
             ['#',' ','#'],
             ['#','#','#'] ], 

            [[' ','#',' '],
             [' ','#',' '],
             [' ','#',' '],
             [' ','#',' '],
             [' ','#',' ']],
            
            [['#','#','#'],
             [' ',' ','#'],
             ['#','#','#'],
             ['#',' ',' '],
             ['#','#','#'] ],

            [['#','#','#'],
             [' ',' ','#'],
             ['#','#','#'],
             [' ',' ','#'],
             ['#','#','#'] ], 
            
            [['#',' ','#'],
             ['#',' ','#'],
             ['#','#','#'],
             [' ',' ','#'],
             [' ',' ','#'] ],
            
            [['#','#','#'],
             ['#',' ',' '],
             ['#','#','#'],
             [' ',' ','#'],
             ['#','#','#'] ],

            [['#','#','#'],
             ['#',' ',' '],
             ['#','#','#'],
             ['#',' ','#'],
             ['#','#','#'] ],

            [['#','#','#'],
             [' ',' ','#'],
             [' ',' ','#'],
             [' ',' ','#'],
             [' ',' ','#'] ],
            
            [['#','#','#'],
             ['#',' ','#'],
             ['#','#','#'],
             ['#',' ','#'],
             ['#','#','#'] ],
            
            [['#','#','#'],
             ['#',' ','#'],
             ['#','#','#'],
             [' ',' ','#'],
             ['#','#','#'] ]]



def display_LED(num):

    for line in range(5): # so a number has come in so it must repeat 5 times for each row of the character
        print() #blank line
        for digit in num:
            for column in range(3):
                if digit == '0':
                    print(pattern[(0)][line][column],end=' ') # print the character but do not jump to a new line after
                elif digit == '1':
                     print(pattern[(1)][line][column],end=' ')
                elif digit == '2':
                     print(pattern[(2)][line][column],end=' ')
                elif digit == '3':
                     print(pattern[(3)][line][column],end=' ')
                elif digit == '4':
                     print(pattern[(4)][line][column],end=' ')
                elif digit == '5':
                     print(pattern[(5)][line][column],end=' ')
                elif digit == '6':
                     print(pattern[(6)][line][column],end=' ')
                elif digit == '7':
                     print(pattern[(7)][line][column],end=' ')
                elif digit == '8':
                     print(pattern[(8)][line][column],end=' ')
                elif digit == '9':
                     print(pattern[(9)][line][column],end=' ')
        #print()

def main():

    number = '-1'

    while int(number) < 0:
        number = input("Enter num: ")
        display_LED(number)

        if number.isnumeric == False:
            number = '-1' # if not a number keep this set to -1 so it will continue to ask for a number



if __name__ == "__main__":
     main()
