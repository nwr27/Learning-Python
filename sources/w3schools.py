# import json
#
# data = open('../Data/data.json')
# data_json = json.load(data)
# print(data_json)
# print(data_json['pasangan1']['umur'])
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import json
import cvzone

data_dict = {"nama": "Nana Wartana", "umur": 22, "hobby": "Seni"}
data_json = json.dumps(data_dict, indent=4, separators=(". ", " = "), sort_keys=True)
print(data_json)
