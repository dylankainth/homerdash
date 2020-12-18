import yaml

def formdatastructure():
    #takes in the data from /main/sampleinput.yaml
    sampleinputfile = open("main/sampleinput.yaml", "r")

    #declares the datastructure in <dict> format using a global;
    #parses the yaml into dict
    global datastructure
    datastructure = (yaml.safe_load(sampleinputfile.read()))

formdatastructure()

def convertdatastructure(key,value,newline = True):
    if newline==True:
        return(key+" = "+value+"\n")
    else:
        return(key+" = "+value)

class write:
    
    global sampleoutputfile

    def init():
        global sampleoutputfile
        sampleoutputfile = open("main/sampleoutput.yaml", "w")

    def settings(): 
        sampleoutputfile.write("[SETTINGS]\n")
        sampleoutputfile.write(   convertdatastructure(   "theme"               ,datastructure["theme"]    ))
        sampleoutputfile.write(   convertdatastructure(   "custom_app_title"    ,datastructure["title"]    ))
        sampleoutputfile.write(   convertdatastructure(   "sidebar_default"     ,"open"    ))
        sampleoutputfile.write(   convertdatastructure(   "background"          ,"https://www.colorhexa.com/"+datastructure["colors"]["dark"]["background"][1:]+".png"     ))
        sampleoutputfile.write("\n \n")
    
    #def users():

    def cards():
        for name in datastructure["services"]:
            print(name)

    def finish():
        sampleoutputfile.close()

#write.init()
#write.settings()
write.cards()
