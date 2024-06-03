import json
import time

# Description: This program converts the contents of a text file into a json object and writes it to a file called json.
#
#
#

print("score-logger service is running...")

request_file = "C:\\Users\\raulp\\Documents\\CS361\\projectfile\\cs361-project\\request.txt"

record_file = "C:\\Users\\raulp\\Documents\\CS361\\projectfile\\cs361-project\\record.txt"

index = 0

def logger():
    global index

    name = str()
    with open(record_file, "r") as infile:

        lines = infile.readlines()

        score = dict()
        last = str()
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
                    score[word] = None
                    last = word
                    isKey = False
                
                else:
                    if isName is True:
                        name = word
                        isName = False
                    score[last] = word
                    isKey = True

    with open(f"score-{name}-{index}.json", 'a') as outfile:
        json.dump(score, outfile)
        index += 1

                
        
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
        logger()
        print('request fulfilled')
        x = open(request_file,'w')
        x.write("request fullfilled")
        x.close()
        


            
    
