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

    #def init():

    def settings():
        sampleoutputfile = open("sampleoutput.yaml", "w")
        sampleoutputfile.write("[SETTINGS]")
        sampleoutputfile.close()
