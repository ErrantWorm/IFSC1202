number=int(input("Enter Length of Time in Days: "))

Years=int(number/365)
Weeks=int((number%365)/7)
Days=int((number%365)%7)

print("Years:",Years)
print("Weeks:",Weeks)
print("Days:",Days)
