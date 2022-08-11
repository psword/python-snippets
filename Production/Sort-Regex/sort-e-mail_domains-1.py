# -*- coding: utf-8 -*-
"""
Spyder Editor
VSCode Editor

This is a script file meant to parse domains and IP addresses.  
Intakes a file called "test.txt" within the same directory as the .py
script file and generates an intermediate file - which can be ignored -
and distills 2 final files.

This version works with the Windows filesystem.
"""

#########################################################################################

# The first function will process the regex search strings.

#########################################################################################

def regex_sort(file):
    

    # This is the file that contains the raw values for cleanup.
    
    file_input_sort = open(file, "rt")
    
    initial_list = []
    characters = {"[", "]", "/", "*", ","}
    
    for line in file_input_sort:
        #Read & replace the string and append to list.
        for character in characters:
            line = line.replace(character, "")
        #print(line)
        initial_list.append(line)
          
    #print(initial_list)
    # Close the input file for read.
    
    file_input_sort.close()

    # Import regex.
    
    import re
    
    # The print function here is solely for testing and console feedback if something goes awry.
    #print("     THIS IS THE 1ST SEPARATOR     ")
    # We define the first regex selection variable.
    

    selection1 = re.compile(r'[0-9a-z-]*\.domain1$|[0-9a-z-]*\.domain2$|[0-9a-z-]*\.domain3$|[0-9a-z-]*\.[0-9a-z-]*\.domain4$|[0-9a-z-]*\.domain5$',re.MULTILINE)
    
    # Create a result based on if there is output for selection1.

    # Define text domain table.
         
    domains_table = []
    
    # Iterate through the lines.
    
    for domains in initial_list:
        # You can uncomment the print function to show what the input is before filtering.
        #print(domains)
        domains = domains[domains.find('@')+1:]
        domains = domains.rstrip()
        results = selection1.findall(domains)
        if results:
            domains_table.append(domains)

    final_list = domains_table

    # We may have duplicates in the list.  Let's filter it.
    
    file_output_path = "c:/temppath/file_output.txt"
    print("\nHere is the output file to review the new items: ", file_output_path, "\n")  
    file_output_sort = open(file_output_path, "wt")
    
    
    global deduplicated
    deduplicated = list(set(final_list))
    
    # Use print to troubleshoot.
    #print(deduplicated)
    print("This is a simple print of the new items (filtered by script:)\n\n", deduplicated)
    
    for element in deduplicated:
        file_output_sort.writelines(element)
        file_output_sort.writelines("\n")
    file_output_sort.close()    



regex_sort(input("Please give the path of the file.  It needs to be a text file.\n"))
