
import pathlib
import re
from reTranslation.models import Payload

def run():
    print("Hello There world")
    pathDic = {}

    # Reading in French payloads:

    payloadType = "portuguese"
    newpath = pathlib.Path('reTranslation/static/portuguese')
    for files in sorted(newpath.rglob("*.*")):
        payloadString = ""
        print(str(files))
        filePath = str(files)
        number = re.sub('\D','',filePath)
        print(number)
        pathDic.update({number:filePath})
        readOut = open(filePath, encoding='utf-8')
        for lines in readOut:
            print(lines)
            payloadString += lines
        print("Going in: "+ payloadString)
        payloadTemp = Payload(programName="portuguese",
                              payloadnumber=number,
                              content=payloadString)
        payloadTemp.save()

'''
    # Reading in Spanish Payloads

    payloadType = "spanish"
    newpath = pathlib.Path('reTranslation/static/spanish')
    for files in sorted(newpath.rglob("*.*")):
        payloadString = ""
        print(str(files))
        filePath = str(files)
        number = re.sub('\D','',filePath)
        print(number)
        readOut = open(filePath, encoding='utf-8')
        for lines in readOut:
            print(lines)
            payloadString += lines
        print("Going in: "+payloadString)
        payloadTemp = Payload(programName="spanish",
                              payloadnumber=number,
                              content=payloadString)
        payloadTemp.save()


'''

