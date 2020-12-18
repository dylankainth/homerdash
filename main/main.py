import yaml

def formdatastructure():
    #takes in the data from /main/sampleinput.yaml
    sampleinputfile = open("main/sampleinput.yaml", "r")

    #declares the datastructure in <dict> format using a global;
    #parses the yaml into dict
    global datastructure
    datastructure = (yaml.safe_load(sampleinputfile.read()))

formdatastructure()

class write:
    
    global sampleoutputfile

    def init():
        global sampleoutputfile
        sampleoutputfile = open("main/sampleoutput.yaml", "w")

    def settings(): 
        sampleoutputfile.write("[SETTINGS]")
        
    
    def finish():
        sampleoutputfile.close()

write.init()
write.settings()
