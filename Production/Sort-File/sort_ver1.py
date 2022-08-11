def sorting(file):
  input_file = open(file)
  words = []
  for line in input_file:
    temp = line.split()
    for element in temp:
      words.append(element)
  input_file.close()
  words.sort()
  output_file = open("use_this_sorted_file.txt", "w")
  for element in words:
    output_file.writelines(element)
    output_file.writelines("\n")
  output_file.close()

sorting(input("Please enter the path to the filename.  Please make it a text file.\n"))