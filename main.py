import json
import time




print("score-logger service is running...")

request_file = "C:\\Users\\raulp\\Documents\\CS361\\projectfile\\cs361-project\\request.txt"

record_file = "C:\\Users\\raulp\\Documents\\CS361\\projectfile\\cs361-project\\record.txt"

global index 

def text_parse():
    """
    This function opens up a text file located at the location defined in 'record_file'. It then iterates through
    the text extracting keys and values from which to insert into a dictionary object which gets converted into a 
    json object after parsing the contents of the text file. 
    
    """
    with open("number.txt", "r") as infile:
        num_str = infile.read()
    index = int(num_str)

    with open("number.txt", "w") as outfile:
        outfile.write(str(index + 1))



    name = str()
    with open(record_file, "r") as infile:

        lines = infile.readlines()

        score = dict()
        key = str()
        isKey = True
        for line in lines:
            words = line.split("'")

            for word in words:
                if word == '':
                    break
                # identifies the name of the player to use it in the file name
                if isKey is True:
                    if word == 'Name':
                        isName = True
                
                    key = word
                    isKey = False
                
                else:
                    if isName is True:
                        name = word
                        isName = False
                    score[key] = word
                    isKey = True
    file_name = f"files\\score-{name}-{index}.json"
    with open(file_name, 'a') as outfile:
        json.dump(score, outfile)

    with open("C:\\Users\\raulp\\Documents\\CS361\\projectfile\\jsontotable\\path.txt", "w") as outfile:
        outfile.write(f"C:\\Users\\raulp\\Documents\\CS361\\projectfile\\score-service\\{file_name}")


   
        
while True:
    time.sleep(0.25)
    with open(request_file, 'r') as infile:
        request = infile.read()
    open(request_file, 'w').close()

    if request == 'log results':
        print('service requested')
        x = open(request_file,'w')
        x.write("request received")
        x.close()
        text_parse()
        print('request fulfilled')
        x = open(request_file,'w')
        x.write("request fullfilled")
        x.close()
        

        


            
    
