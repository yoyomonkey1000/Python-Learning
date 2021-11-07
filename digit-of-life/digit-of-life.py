# digits of life
# get a string of numbers and add each digit up and print out total. 
# keep repeating until there is one digit

def digSum( n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10 # do a modulus of 0 and any remainder add it to the sum
        n //= 10 #floor division so you drop the unit and assign it back to n
    
    return sum
 

n = 19991229
print (digSum(n))