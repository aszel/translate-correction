import json

def martin(d, key):
    for k, v in d.items():
        if not key:
            key = k
        else:
            key = "." + k
        if isinstance(v, dict):
            martin(v, key)
        else:
            print(key,"{0} : {1}".format(k, v))


with open('test.json') as json_file:
    data = json.load(json_file)
    print(data)
    martin(data, '')
    pass
