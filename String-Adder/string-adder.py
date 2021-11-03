# String Adder gets a list of numbers seperated by 
# spaces and adds them up and output the result
# Jazz

numbers_string = input("Please input numbers seperated by a space ")
number_list = numbers_string.split()
total = 0

try:
    for num in number_list:
        print("Adding ", str(num) , " to " ,  str(total))
        total += float(num)
    print(f"Total is {total}" )

except: 
    print(f"{num} is not a number")
