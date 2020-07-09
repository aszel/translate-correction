import json
import os

inputFile = "output/duplicates.test.json"
#inputFile = "output/duplicates.de.json"
outputFile = "output/inter-language-duplicates.json"

myLanguages = ["en", "pl"]


def get_key_for_lang(language, key):
    result = {}
    f = open("output/duplicates." + language + ".json", "r")
    myDict = json.load(f)
    for k,values in myDict.items():
        if key in values:
            return values
    f.close()
    pass

# read first key for each value and check if it is around in the other languages, too
def get_inter_lang_keys(languages, sourceDict):
    myInterLanguageKeys = {}
    for k, v in sourceDict.items():
        entry = {}
        firstValue = v[0]
        entry['de'] = v
        for language in languages:
            values = get_key_for_lang(language, firstValue)
            entry[language] = values
        myInterLanguageKeys[firstValue] = entry
    return myInterLanguageKeys

def write_output_file(inputData):
    if os.path.exists(outputFile):
        os.remove(outputFile)
    f = open(outputFile, "a")
    f.write(json.dumps(inputData))
    f.close()

with open(inputFile) as json_file:
    data = json.load(json_file)
    myInterLanguageKeys = get_inter_lang_keys(myLanguages, data)
    write_output_file(myInterLanguageKeys)
