# OVERVIEW
This program works by scanning a text file and searching for the key words "log results". Upon reading those keywords, the program then reads from another text file and iterates through the text 
assigning keys for a dictionary object followed by it's value. The program then converts the dictionary into json a file assigning the file name by concatenating 'score-' + the value of the key 'Name' + '-' + a unique number. The json files is then ready for export by whatever program wants it. 


# HOW TO REQUEST DATA
To request service/data from th service, a program must write "log results" into the a text file that the score-service program can read. It is important to ensure that the request_file and reqcord_file variables are updated to reflect the actual complete pathways for where those files will be located. 


# HOW TO RECEIVE DATA
The receive data, a program must use the file located at the request_file pathway. Aside from creating a json file, the only data that this program sends are the following messages:
  'request recieved' - sent after reading the 'log results' request
  'request fulfilled' - sent after completeing the complete execution of creating and populating the json file with the text file contents

# REQUIREMENTS
In order for the program to correctly parse the text file and build the equivalent json object/file, The contents of the text file must be formatted in this fashion:

'somekey''somevalue''someotherkey''someothervalue''anotherkey''anothervalue'.....

# UNIQUE NUMBER IN FILE NAME
The number.txt file in the repository serves the purpose of keeping a running count of each json file ever created by the program. This number is used to define and increment the 'index' variable which is concatenated to each json file name in order to ensure a unique json file for each entry.
