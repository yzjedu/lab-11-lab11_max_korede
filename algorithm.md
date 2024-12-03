# Algorithm Document


* Purpose: Convert the morse code file into a dictionary
* Name: read_file_to_dict
* Parameters: filename
* Return: Dictionary of morse code
* Algorithm:
  1. Make an empty dictionary 
  2. set input file equal to open filename
  3. For line in input file
     1. Split the lines by the tab that separates the letters from the morse code
     2. Add to the dictionary the letter using the morse code as they key
  4. Return dictionary


* Purpose: create a table
* Name:read_code_to_table
* Parameters: Filename 
* Return:table
* Algorithm:
  1. create a blank table
  2. set input file equal to open filename
  3. set data equal to a list where each item is a line 
  4. For each line in data
     1. Split the line by spaces and set to row
     2. add row onto table
  3. Return the table

* Purpose: create a dictionary
* Name:convert_table_to_words
* Parameters: dictionary, table 
* Return:table
* Algorithm:
  1. for every list in the table
     2. for every item in the list
        3. replace item in list with its corresponding character
  2. return table

* Purpose: reorganize table
* Name: reorganize_table
* Parameters: table 
* Return: new_table
* Algorithm:
  1.  Create blank list called new table
  2. create blank list called temp_list
  3. for line in table
     4. for item in line
        5. add the first item in the row to temp_list
     6. add the value of temp_list to new table
     7. set temp_list to empty
  4. return new table

* Purpose: open a new file to write in
* Name:create_new_file
* Parameters: table, filename 
* Return: nothing
* Algorithm:
  1. open the file chosen in the write mode and set to data file
  2. set temp string to blank quotes
  3. for line in table 
    4. for letter in line
       5. add value of letters to temp_string
    6. add a new line to temp_string
    7. write value of temp string onto data_file
    8. set temp string to blank
  9. close data_file























