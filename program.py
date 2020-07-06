import json

myTranslations = {}
myTranslationsFlipped = {}

def get_key_values(myDict, prevKey):
    for k, v in myDict.items():
        if isinstance(v, dict):
            get_key_values(v, prevKey + '.' + k)
        else:
            #print(prevKey + '.' + k, v)
            myTranslations[prevKey + '.' + k] = v

def generate_flipped_dictionary(myDict):
    for key, value in myDict.items():
        if value not in myTranslationsFlipped:
            myTranslationsFlipped[value] = [key]
        else:
            myTranslationsFlipped[value].append(key)

def get_multi_assigned_values(myDict):
    for key, value in myDict.items():
        if len(value)>1:
            print(key, value)

with open('test.json') as json_file:
    data = json.load(json_file)
    print("The data")
    print(data)
    print("---")
    get_key_values(data, '')
    print(myTranslations)
    print("---")
    generate_flipped_dictionary(myTranslations)
    print(myTranslationsFlipped)
    print("---")
    # print keys of flippped dict. witch have several entries in value array
    get_multi_assigned_values(myTranslationsFlipped)
    pass
