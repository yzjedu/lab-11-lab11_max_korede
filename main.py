# Name: read_file_to_dict
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
# Using the table made from the read_code_to_table function
# and the dictionary from the read_file to dict function,
# creates a new table by converting the morse code to English
def convert_table_to_words(dictionary, table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = dictionary[table[i][j]]
    return table

# Name: reorganize_table
# Because the table that is made from convert_table_to_letters
# converts puts the letters into lists (creating a table with a
# list of lists), this function reverses that so that the table
# doesn't contain internal lists inside the external ones
def reorganize_table(table):
    new_table = []
    temp_list = []
    for line in table:
        for item in line:
            temp_list.append(item[0])
        new_table.append(temp_list)
        temp_list = []
    return new_table

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


def main():
    print("Welcome to our morsecode converter! We have a few files for you to convert.\n"
          "But first, please enter the name of the file that contains the conversions")
    convert_file = str(input(""))
    morse_dictionary = read_file_to_dict(convert_file)
    print("What file would you like to convert?")
    morse_file = str(input(""))
    letters = read_code_to_table(morse_file)
    table = convert_table_to_words(morse_dictionary, letters)
    finish = reorganize_table(table)
    name = str(input("What should be the name of the new file? "))
    create_new_file(finish, name)

main()