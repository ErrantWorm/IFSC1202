import csv
with open("09.Project Distances.csv", "r") as file:
    reader = csv.reader(file)
    distance_table = [row for row in reader]


print("Distance Table:")
for row in distance_table:
    print("".join(f"{item:15}" for item in row)) 

while True:
    
    from_city = input("\nEnter the From City (or press Enter to quit): ").strip()
    if not from_city:
        print("Exiting program.")
        break

    to_city = input("Enter the To City: ").strip()
    
    from_city_index = -1
    to_city_index = -1
    
    for i in range(1, len(distance_table)):  
        if distance_table[i][0].strip().lower() == from_city.lower():
            from_city_index = i
            break
    
    for j in range(1, len(distance_table[0])):  
        if distance_table[0][j].strip().lower() == to_city.lower():
            to_city_index = j
            break

    if from_city_index == -1:
        print("Invalid From City")
    elif to_city_index == -1:
        print("Invalid To City")
    else:
        distance = distance_table[from_city_index][to_city_index]
        print(f"The distance from {from_city} to {to_city} is {distance}.")
