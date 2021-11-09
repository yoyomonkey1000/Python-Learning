# digits of life
# get a string of numbers and add each digit up and print out total. 
# keep repeating until there is one digit

def dig_sum(number):
    sum = 0
     
    while(number != 0 or (int(len(str(sum)))) > 1 or sum == 0):
     
        #if(number == 0):
         #   n = sum
         #   sum = 0
         
        sum += number % 10 # do a modulus of 0 and any remainder add it to the sum
        number //= 10 #floor division so you drop the unit and assign it back to n
        print(sum)
    
    return sum
 
def main():
    n = int(input("Enter your number "))
    final_num = (dig_sum(n))
    print(f"The final number is {final_num}")

if __name__ == "__main__":
    main()