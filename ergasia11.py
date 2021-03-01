import json
file = open("dictionary.txt", "r")
cont = file.read()
dicti = json.loads(cont)
file.close()
freq={}
def get_all_keys(dictio):
    for m, value in dictio.items():
        if type(value) is dict:
            get_all_keys(value)
            if (m in freq):
                freq[m] += 1
            else:
                freq[m]=1
        elif (m in freq):
            freq[m] += 1
        else:
            freq[m]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    get_all_keys(value[i])
get_all_keys(dicti)
maxvalue = max(freq.items(), key=lambda x: x[1])
maxfreq = list()
for key, value in freq.items():
    if value == maxvalue[1]:
        maxfreq.append(key)
print(maxfreq)
