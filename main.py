# Programmers:  Max Rice and Korede Oni
  # Course:  CS151, Professor Yalew
  # Due Date: 11-28-24
  # Lab Assignment:  11
  # Problem Statement:  Someone has converted your files using a cipher. Ciphers have been very popular
  #                     for millennia as a way to hide information. Can you create a program to convert
  #                     them back to plain English??
  # Data In: The name of the file that contains the morse code to English conversions, the name of the file
  #          containing morse code that the user wants to convert to English, the name of the new file with the
  #          translated morse code
  # Data Out:  A new file containing the English translation of one of the morse code files
  # Credits: Class

# Import OS module
import os

# Name: read_file_to_dict
# Parameter(s): The name of the file to be read
# Makes a dictionary and fills said dictionary with data from
# the input file by splitting each line via the double space
def read_file_to_dict(filename):
    morse_dict = {}
    input_file = open(filename, "r")
    for line in input_file:
        items = line.split('  ')
        key = items[1].strip()
        value = items[0].split()
        morse_dict[key] = value
    input_file.close()
    return morse_dict

# Name: read_code_to_table
# Parameter(s): The name of the file to be read
# Creates a table with a preexisting file where each list
# in the table is a line in the file that is split by spaces
def read_code_to_table(filename):
    table = []
    input_file = open(filename, "r")
    data = input_file.readlines()
    for line in data:
        row = line.split()
        table.append(row)
    return table

# Name: convert_table_to_words
# Parameter(s): The dictionary that holds all the conversions
#               and a table to convert to English
# Using the table made from the read_code_to_table function
# and the dictionary from the read_file to dict function,
# creates a new table by converting the morse code to English
def convert_table_to_words(dictionary, table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = dictionary[table[i][j]]
    return table

# Name: reorganize_table
# Parameter(s): the table that is in need of reorganization
# Because the table that is made from convert_table_to_letters
# converts puts the letters into lists (creating a table with a
# list of lists), this function reverses that so that the table
# doesn't contain internal lists inside the external ones
# (e.g. convert [[['A'], ['B'], ['C']]] to [['A', 'B', 'C']])
def reorganize_table(table):
    new_table = []
    temp_list = []
    for line in table:
        for item in line:
            temp_list.append(item[0])
        new_table.append(temp_list)
        temp_list = []
    return new_table

# Name: create_new_file
# Parameter(s): table to print to new file, name of new file
# Creates a new file with the translated version of the file chosen
# by the user, requires the table made from reorganize_table and
# input by user for the name
def create_new_file(table, filename):
    data_file = open(filename, 'w')
    temp_string = ""
    for line in table:
        for letters in line:
            temp_string += letters
        temp_string += "\n"
        data_file.write(temp_string)
        temp_string = ""
    data_file.close()

# Name: main
# Parameter(s): None
# Function that allows program to run
def main():
    print("Welcome to our morse code converter! In this program, we will be taking a file written\n"
          "entirely in morse code, then write it out on a new file that you get to name!")
    print("")
    get_convert = str(input("Before we can do anything, we need to be able to easily convert morse code to characters.\n"
                             "Please enter the name of the file that contains the conversions of morse code to English.\n"
                            "(Note: You do NOT need to include '.txt' in your input, but you may do so if you would like)\n"
                            "What is the conversion file name?: "))
    if get_convert[-4:] != ".txt":
        get_convert += ".txt"
    while not os.path.isfile(get_convert) or get_convert != 'morsecode.txt':
        print("")
        print("There was an error getting that file. Either the file does not exist or the inputted file cannot be used for this task. Please try again.")
        get_convert = input("Please enter the name of the file that contains the conversions.\n"
                            "(Note: You do NOT need to include '.txt' in your input, but you may do so if you would like)\n"
                            "What is the conversion file name?: ")
        if get_convert[-4:] != ".txt":
            get_convert += ".txt"
    morse_dictionary = read_file_to_dict(get_convert)
    print("")
    morse_file = str(input("We have a few options for file you can convert. What file would you like to convert to readable characters?\n"
                           "Your options for files are: morse1.txt, morse2.txt, or morse3.txt\n"
                           "(Note: You do NOT need to include '.txt' in your input, but you may do so if you would like)\n"
                           "What is the file you would like to convert? "))
    if morse_file[-4:] != ".txt":
        morse_file += ".txt"
    while not os.path.isfile(morse_file) or (morse_file != 'morse1.txt' and morse_file != 'morse2.txt' and morse_file != 'morse3.txt'):
        print("")
        print("There was an error getting that file. Either the file does not exist or the inputted file cannot be used for this task. Please try again.")
        morse_file = input("What file do you want to convert to readable characters?\n"
                           "Your options for files are: morse1.txt, morse2.txt, or morse3.txt\n"
                           "(Note: You do NOT need to include '.txt' in your input, but you may do so if you would like)\n"
                           "What is the file you would like to convert? ")
        if morse_file[-4:] != ".txt":
            morse_file += ".txt"
    characters = read_code_to_table(morse_file)
    converted_morse = reorganize_table(convert_table_to_words(morse_dictionary, characters))
    print("")
    new_filename = str(input("Nice! Now that we have everything, it's time for you to give this new file a name.\n"
                             "What should be the name of the new file?\n"
                             "(Note: You do NOT need to include '.txt' in your input, but you may do so if you would like)\n"
                             "Please enter a name for the file: "))
    if new_filename[-4:] != ".txt":
        new_filename += ".txt"
    create_new_file(converted_morse, new_filename)
    print("")
    print("All done, now your file converted and is ready to go! Give it a read if you got the time!\n"
          "Thank you for using our morse code converter!")

# Main function call
main()


