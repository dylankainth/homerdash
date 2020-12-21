import yaml
import json
from urllib.parse import urlparse

homerfiledirectory = "sampledata/homer/"
dashmachinefilleddirectory = "sampledata/dashmachine/"


def formdatastructure():
    #takes in the data from the variable-declared directory
    sampleinputfile = open(homerfiledirectory+"config.yml", "r")

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
        sampleoutputfile = open(dashmachinefilleddirectory+"config.ini", "w")

    def settings(): 
        sampleoutputfile.write("[Settings]\n")
        sampleoutputfile.write(   convertdatastructure(   "theme"               ,datastructure["theme"]    ))
        sampleoutputfile.write(   convertdatastructure(   "custom_app_title"    ,datastructure["title"]    ))
        sampleoutputfile.write(   convertdatastructure(   "sidebar_default"     ,"open"    ))
        sampleoutputfile.write(   convertdatastructure(   "tags_expanded"       ,"True"    ))
        sampleoutputfile.write(   convertdatastructure(   "accent"       ,"blue"    ))
        sampleoutputfile.write(   convertdatastructure(   "background"          ,"https://www.colorhexa.com/"+datastructure["colors"]["dark"]["background"][1:]+".png"     ))

        #This section is for icons. Unfortunately, Homer uses Font-Awesome while DashMachine uses Google Material Design Icons.
        #Therefore, it is hard to translate. 
        #This code gives a start, and is able to translate some Font-Awesome to Material Design icons BY CHANCE ALONE.

        #icondictionary=""
        #for classification in datastructure["services"]:
            #icondefinition = {"name": classification["name"],"icon": classification["icon"]}
            #icondictionary = icondictionary+json.dumps(icondefinition)+","
        #sampleoutputfile.write(   convertdatastructure(    "tags"               ,(icondictionary[0:-1])))
        #sampleoutputfile.write("\n \n")

    def cards():
        for classification in datastructure["services"]:
            for item in classification["items"]:
                sampleoutputfile.write("["+item["name"]+"]\n")
                sampleoutputfile.write(   convertdatastructure(   "prefix"               ,((urlparse(item["url"])).scheme)+"://"    ))
                sampleoutputfile.write(   convertdatastructure(   "url"               ,((urlparse(item["url"])).netloc)+((urlparse(item["url"])).path)))
                sampleoutputfile.write(   convertdatastructure(   "description"               ,item["subtitle"]    ))
                sampleoutputfile.write(   convertdatastructure(   "open_in"               , "new_tab"    ))
                sampleoutputfile.write(   convertdatastructure(   "icon"               , "static/images/icons/"+(item["logo"]).lstrip("assets/tools/")    ))
                sampleoutputfile.write(   convertdatastructure(   "sidebar_icon"               , "static/images/"+(item["logo"]).lstrip("assets/tools/")    ))
                sampleoutputfile.write(   convertdatastructure(   "tags"               , classification["name"]))
                #url queries, parameters and fragments are not supported, but they could be by ajusting the code above
                #sampleoutputfile.write(   convertdatastructure(   "url"    ,(urlparse(item["url"]))    ))
                sampleoutputfile.write("\n")
            sampleoutputfile.write("\n\n")

    def finish():
        sampleoutputfile.close()

write.init()
write.settings()
write.cards()
write.finish()