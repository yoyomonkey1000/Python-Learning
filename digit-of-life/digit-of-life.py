# digit of life
# get a string of numbers add them up
# keep adding the digits until its a single digit

number = "13"
number_list = number.split()

digits = 0
total = 0

#if True:
while digits != 1:
    for num in number_list:
        total += (int(num))
        digits = int(len(str(total)))
    number_list = str(total) 
    number_list = number_list.split()  


print(digits)

print("Final Total is ", total)

