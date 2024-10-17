
def ParseDegreeString(ddmmss):
   
    degree_symbol_pos = ddmmss.find(chr(176))  # Degree symbol (°)
    minute_symbol_pos = ddmmss.find("'")       # Minute symbol (')
    second_symbol_pos = ddmmss.find('"')       # Second symbol (")

    
    degrees = float(ddmmss[:degree_symbol_pos])  # Get degrees as a float
    minutes = float(ddmmss[degree_symbol_pos + 1:minute_symbol_pos])  # Get minutes as a float
    seconds = float(ddmmss[minute_symbol_pos + 1:second_symbol_pos])  # Get seconds as a float

    
    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):

    
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def convert_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                
                ddmmss = line.strip()

                degrees, minutes, seconds = ParseDegreeString(ddmmss)

               
                decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)

                outfile.write(f"{decimal_degrees}\n")


input_file = '07.Project Angles Input.txt'
output_file = '07.Project Angles Output.txt'  


convert_file(input_file, output_file)
