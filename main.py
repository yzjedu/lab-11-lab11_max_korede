def write_file_to_dict(filename):
    dict = {}
    input_file = open(filename, "r")
    for line in input_file:
        items = line.split('  ')
        key = items[1].strip()
        value = items[0].split()
        dict[key] = value
    input_file.close()
    return dict

print(write_file_to_dict("morsecode.txt"))