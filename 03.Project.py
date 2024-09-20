firstN = float(input("Enter First Number: "))
operator = input(("Enter Operator (+,-,*,/): "))
secondN = float(input("Enter Second Number: "))

if operator == "+":
    result = firstN + secondN
    print(round(result, 2))

elif operator =="-":
    result = firstN - secondN
    print(round(result, 2))

elif operator =="*":
    result = firstN * secondN
    print(round(result, 2))

elif operator =="/":
    result = firstN / secondN
    print(round(result, 16))

else: 
    print("Invaild operator")