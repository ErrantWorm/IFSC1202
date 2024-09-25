# Program to find special numbers in a range

# Get the range from the user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Function to calculate the sum of digits raised to the power of number of digits
def is_special_number(num):
    temp = num
    digits = 0
    # Find the number of digits
    while temp > 0:
        digits += 1
        temp //= 10
    
    # Reset temp to the original number
    temp = num
    sum_of_powers = 0
    
    # Calculate the sum of digits raised to the power of number of digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    
    # Check if the sum equals the original number
    return sum_of_powers == num

# Loop through the range and print special numbers
print(f"Special numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if is_special_number(i):
        print(i)
