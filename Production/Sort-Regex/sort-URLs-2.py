# -*- coding: utf-8 -*-
"""
Spyder Editor
VSCode Editor

This is a script file meant to parse domains and IP addresses.  
Intakes a file called "test.txt" within the same directory as the .py
script file and generates an intermediate file - which can be ignored -
and distills 2 final files.

This version works with the Windows and Linux filesystems.
"""

#########################################################################################

# The first function will process the regex search strings.

#########################################################################################

def regex_sort(file):
    
    # This is the file that contains the raw values for cleanup.
    
    file_input_sort = open(file, "rt")
    
    initial_list = []
    characters = {"[", "]", "/", "*.", "www.", "www[.]"}
    
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

    #for domains in selection1:
    #    domains = domains.rstrip()
    #    domains_table.append(domains)
    
    for domains in initial_list:
        domains = domains.rstrip()
        results = selection1.findall(domains)
        if results:
            domains_table.append(domains)
    
    # Create a table for IPs.
    
    IPs_table = []
    
    # We define the second regex selection variable.
    
    selection2 = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
    
    # We create the if block to append to the list.
    
    for IPs in initial_list:
        IPs = IPs.rstrip()
        results = selection2.match(IPs)
        if results:
            IPs_table.append(IPs)

    # The print function here is solely for testing and console feedback if something goes awry.
    #print("     THIS IS THE 2ND SEPARATOR     ")
    #print(IPs_table)
    
    # Merge the lists.

    final_list = domains_table + IPs_table

    # We may have duplicates in the list.  Let's filter it.
    
    file_output_sort = open("sort_result.txt", "wt")
    
    global deduplicated
    deduplicated = list(set(final_list))
    
    # Use print to troubleshoot.
    #print(deduplicated)
    print("This is a simple print of the new items (filtered by script:)\n\n", deduplicated)
    
    for element in deduplicated:
        file_output_sort.writelines(element)
        file_output_sort.writelines("\n")
    file_output_sort.close()    



regex_sort(input("Please give the path of the input file that contains the addresses we are adding.  It needs to be a text file.\n"))

#########################################################################################

# This function will accept the path to the master list.

#########################################################################################

global listpath
listpath = input("Please give the path of the master list.  It needs to be a text file.\n")

#########################################################################################

# This function will sort the output and merge it with the existing master list.

#########################################################################################

def combination():

    user_input_path = listpath
    file_input_combo = open(user_input_path, "rt")

    fw_list = []

    for element in file_input_combo:
        temp = element.split()
        for line in temp: 
            fw_list.append(temp)
      
    file_input_combo.close()

    file_input1_combo = open("sort_result.txt","rt")
    
    for element in file_input1_combo:
        temp = element.split()
        for line in temp:
            fw_list.append(temp)
    
    file_input1_combo.close()
    
    fw_list.sort()
    
    file_output_combo = open(user_input_path, "wt")
    for element in fw_list:
      file_output_combo.writelines(element)
      file_output_combo.writelines("\n")

    file_output_combo.close()

combination()

#########################################################################################


# This function will process the master list and remove duplicates, then sort.


#########################################################################################

def masterlistsort():

    master_list = []

    user_input_path = listpath
    master_list_read = open(user_input_path, "rt")

    for element in master_list_read:
        temp = element.split()
        for line in temp:
            master_list.append(temp)

    master_list_read.close()

    master_list.sort()
    master_list_dedupe = []
    [master_list_dedupe.append(line) for line in master_list if line not in master_list_dedupe]

    master_list_write = open(user_input_path, "wt")

    for element in master_list_dedupe:
      master_list_write.writelines(element)
      master_list_write.writelines("\n")

    master_list_write.close()

masterlistsort()