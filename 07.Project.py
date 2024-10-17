# Function to parse the degree string and return degrees, minutes, and seconds as floats
def ParseDegreeString(ddmmss):
    # Find the positions of the degree, minute, and second symbols
    degree_symbol_pos = ddmmss.find(chr(176))  # Degree symbol (°)
    minute_symbol_pos = ddmmss.find("'")       # Minute symbol (')
    second_symbol_pos = ddmmss.find('"')       # Second symbol (")

    # Extract degrees, minutes, and seconds using string slicing
    degrees = float(ddmmss[:degree_symbol_pos])  # Get degrees as a float
    minutes = float(ddmmss[degree_symbol_pos + 1:minute_symbol_pos])  # Get minutes as a float
    seconds = float(ddmmss[minute_symbol_pos + 1:second_symbol_pos])  # Get seconds as a float

    # Return degrees, minutes, and seconds as floating point numbers
    return degrees, minutes, seconds

# Function to convert degrees, minutes, and seconds to decimal degrees
def DDMMSStoDecimal(degrees, minutes, seconds):
    
    # Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

# Function to read the file, convert the angles, and write them to a new file
def convert_file(input_file, output_file):

    # Open the input file in read mode
    with open(input_file, 'r') as infile:

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:

            # Read each line from the input file
            for line in infile:
                # Remove any leading/trailing spaces
                ddmmss = line.strip()

                # Parse the DMS string into degrees, minutes, and seconds
                degrees, minutes, seconds = ParseDegreeString(ddmmss)

                # Convert to decimal degrees
                decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)

                # Write the decimal degree value to the output file
                outfile.write(f"{decimal_degrees}\n")

# Main part of the code: specifying input and output file names
input_file = '07.Project Angles Input.txt'
output_file = '07.Project Angles Output.txt'  

# Call the function to convert the file
convert_file(input_file, output_file)
