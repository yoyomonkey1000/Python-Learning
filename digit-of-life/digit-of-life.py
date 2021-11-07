# Python program to find sum of
# digits of a number until
# sum becomes single digit.
 

# method to find sum of digits
# of a number until sum becomes
# single digit
def digSum( n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n //= 10
    
    return sum
 
# Driver method
n = 1234567689234234234234234
print (digSum(n))