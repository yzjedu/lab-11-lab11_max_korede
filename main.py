def write_file_to_dict(filename):
    morse_dict = {}
    input_file = open(filename, "r")
    for line in input_file:
        items = line.split('  ')
        key = items[1].strip()
        value = items[0].split()
        morse_dict[key] = value
    input_file.close()
    return morse_dict

lem = write_file_to_dict("morsecode.txt")

def read_code_to_table(filename):
    table = []
    input_file = open(filename, "r")
    data = input_file.readlines()
    for line in data:
        row = line.split()
        table.append(row)
    return table

def convert_table_to_morse(dictionary, table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = dictionary[table[i][j]]
    return table

def reorganize_table(table):
    new_table = []
    temp_list = []
    for line in table:
        for item in line:
            temp_list.append(item[0])
        new_table.append(temp_list)
        temp_list = []
    return new_table

domo = read_code_to_table("morse1.txt")

masa = convert_table_to_morse(lem, domo)

print(read_code_to_table("morse1.txt"))
print(masa)
print(reorganize_table(masa))