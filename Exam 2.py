names_list = []
with open("Exam Two Names.txt", "r") as file:
    rank = 1
    for line in file:
     
        boy_name, girl_name = line.split(",")
        boy_name = boy_name.strip()
        girl_name = girl_name.strip()
        
        names_list.append([rank, boy_name, girl_name])
        
        rank += 1

def format_name(name):
    return name.strip().capitalize()


while True:
    
    user_name = input("Enter a name (or 'Q' to quit): ").strip()
    if user_name.lower() == "q":
        print("Exiting program.")
        break

    user_name = format_name(user_name)

    found = False

    for entry in names_list:
        rank = entry[0]
        boy_name = entry[1]
        girl_name = entry[2]
        
        if user_name == boy_name:
            print(f"Boy's Name - Rank: {rank}")
            found = True
            break 
        
        elif user_name == girl_name:
            print(f"Girl's Name - Rank: {rank}")
            found = True
            break  
    
    if not found:
        print("Name Not Found.")
