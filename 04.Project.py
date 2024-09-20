l = int(input("Enter the start of the range: "))
h = int(input("Enter the end of the range: "))

print(f"Prime numbers between {l} and {h} are:")

# Iterate through the specified range
for num in range(l, h + 1):
    if num > 1:  # Prime numbers must be greater than 1
        is_prime = True  # Assume num is prime
        for i in range(2, (num // 2) + 1):
            if num % i == 0:  # num is divisible by i, so it's not prime
                is_prime = False
                break  # Exit the loop if it's not prime
        if is_prime:
            print(num, end=' ')  # Only print if num is prime
        
                
