import json
import os

# Script reads json file and writes
# all keys which hold duplicate values to an output file
# example:
#  duplicatedValue: [global.trivial.key.foo, global.trivial.key.bar]
#
currentLanguage = "de"
#currentLanguage = "en"
#currentLanguage = "pl"
inputFile = "input/" + currentLanguage + ".json"
outputFile = "output/duplicates." + currentLanguage + ".json"

myTranslations = {}
myTranslationsFlipped = {}

def get_key_values(myDict, prevKey):
    for k, v in myDict.items():
        if isinstance(v, dict):
            if prevKey == '':
                get_key_values(v, k)
            else:
                get_key_values(v, prevKey + '.' + k)
        else:
            myTranslations[prevKey + '.' + k] = v

def generate_flipped_dictionary(myDict):
    for key, value in myDict.items():
        if value not in myTranslationsFlipped:
            myTranslationsFlipped[value] = [key]
        else:
            myTranslationsFlipped[value].append(key)

def get_multi_assigned_values(myDict):
    if os.path.exists(outputFile):
        os.remove(outputFile)
    f = open(outputFile, "a")
    duplicates = 0
    items_with_duplicates = 0;
    for key, values in myDict.items():
        if len(values)>1:
            items_with_duplicates += 1
            duplicates += len(values)
            my_values_string = '","'.join(values)
            f.write('"' + key + '"' + ':' + '["'+ my_values_string + '"],\n')
    avg_duplicates = duplicates / items_with_duplicates
    print("Duplicates: ", duplicates)
    f.close()

with open(inputFile) as json_file:
    data = json.load(json_file)
    get_key_values(data, '')
    generate_flipped_dictionary(myTranslations)
    get_multi_assigned_values(myTranslationsFlipped)
    pass
