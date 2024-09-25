start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

def is_special_number(num):
    temp = num
    digits = 0
    
    while temp > 0:
        digits += 1
        temp //= 10

    temp = num
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    
    return sum_of_powers == num

print(f"Special numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if is_special_number(i):
        print(i)
