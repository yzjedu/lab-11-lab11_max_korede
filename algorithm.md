# Algorithm Document


* Purpose: Convert the morse code file into a dictionary
* Name: Convert_file_to_dict
* Parameters: File that needs to be read 
* Return: Dictionary of morse code
* Algorithm:
    1. Make an empty dictionary
    2. For line in fine
       1. Split the lines by the tab that separates the letters from the morse code
       2. Add to the dictionary the letter using the morse code as they key
    3. Return dictionary


* Purpose: To read morse code file and convert into letters
* Name: file_to_letters
* Parameters: File that we're reading and dictionary
* Return: The file as letters
* Algorithm:
  1. For each line in file
     1. Split the line by spaces
  2. For each piece of morse code
     1. Find as a letter and add it to a new list
  3. Return the list


* Purpose: To write letters to a new file
* Name: Write_letters_to_file
* Parameters: List that we're writing to and file name
* Algorithm:
  1. Open file to write in
  2. For each list in table
     1. Write letters as a string with a new line when starting another list
  3. Close file


* Purpose: To execute all the code
* Name: Name
* Parameters: None
* Algorithm:
  