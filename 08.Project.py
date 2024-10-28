
with open("Constitution.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

while True:
  
    search_term = input("Enter a search term (or press Enter to quit): ").strip()
    if not search_term:
        print("Exiting program.")
        break
    
    found = False
    i = 0
    while i < len(lines):
        
        if search_term.lower() in lines[i].lower():
            found = True
           
            start = i
            while start > 0 and lines[start - 1] != "":
                start -= 1
            
           
            end = i
            while end < len(lines) - 1 and lines[end + 1] != "":
                end += 1
            

            print(f"\n--- Section found (starts at line {start + 1}) ---")
            for j in range(start, end + 1):
                print(lines[j])
            print("--- End of section ---\n")

         
            i = end
        i += 1

    if not found:
        print("No results found for the search term.")
