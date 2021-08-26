
import pathlib
import re

def run():
    print("Hello There world")
    pathDic = {}
    payloadType = "french"
    newpath = pathlib.Path('reTranslation/static/french')
    for files in sorted(newpath.rglob("*.*")):
        print(str(files))
        filePath = str(files)
        number = re.sub('\D','',filePath)
        print(number)
        pathDic.update({number:filePath})
    payloadType = "spanish"
    newpath = pathlib.Path('reTranslation/static/spanish')
    for files in sorted(newpath.rglob("*.*")):
        print(str(files))
        filePath = str(files)
        number = re.sub('\D','',filePath)
        print(number)




