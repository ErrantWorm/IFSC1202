input_file = open("06.Project Input File.txt", "r")
output_file = open("06.Project Output File.txt", "w")
merge_file = open("06.Project Merge File.txt", "r")


input_count = 0
merge_count = 0
output_count = 0


for line in input_file:
    
    
    
    if '**Insert Merge File Here**' in line:
        
        for merge_line in merge_file:
            output_file.write(merge_line)
            merge_count += 1
            output_count += 1
    else:
        
        output_file.write(line)
        input_count += 1
        output_count += 1

input_file.close()
merge_file.close()
output_file.close()


print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")
