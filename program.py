import json

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
    f = open("duplicates.de.txt", "a")
    duplicates = 0
    items_with_duplicates = 0;
    for key, values in myDict.items():
        if len(values)>1:
            items_with_duplicates += 1
            duplicates += len(values)
            my_values_string = ';'.join(values)
            f.write(key + ':' + '['+ my_values_string + ']\n')
    avg_duplicates = duplicates / items_with_duplicates
    print("duplicates: ", duplicates)
    print("avg duplicates: ", avg_duplicates)
    f.close()

with open('de.json') as json_file:
    data = json.load(json_file)
    #print("The data")
    #print(data)
    #print("---")
    get_key_values(data, '')
    #print(myTranslations)
    #print("---")
    generate_flipped_dictionary(myTranslations)
    #print(myTranslationsFlipped)
    #print("---")
    # print keys of flippped dict. witch have several entries in value array
    get_multi_assigned_values(myTranslationsFlipped)
    pass
