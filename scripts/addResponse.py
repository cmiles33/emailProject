from reTranslation.models import Reponse,Program, Payload

# There are 0 - 355 French payloads
# There are 0 - 195 Spanish payloads

import pathlib
import re
from reTranslation.models import Payload, Reponse, Program

def run():
    print("Adding Responses")
    pathDic = {}

    # Reading in French payloads:

    payloadType = "french"
    newpath = pathlib.Path('reTranslation/static/french')
    for files in sorted(newpath.rglob("*.*")):
        payloadString = ""
        print(str(files))
        filePath = str(files)
        number = re.sub('\D','',filePath)
        print(number)
    # Get the users program object
    # create response Object
    # asociate payload object with resposne object
    # save resposne object
