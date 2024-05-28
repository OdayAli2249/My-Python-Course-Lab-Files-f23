import math

input_str = input("Enter rent days:")

input_num = int(input_str)

div = input_num / 30
mod = input_num % 30

f_div = math.floor(div)

res = 0
if(f_div >= 3):
    res = f_div * 20000 + mod * 1000
elif(f_div == 2):
    res = f_div * 25000 + mod * 1000
elif(f_div == 1):
    res = f_div * 30000 + mod * 1000

print ('Result: ',res)
    