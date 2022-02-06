import json
from simplerandomgenerator import SimpleRandomGenerator

''' Generate sample config to test functionality '''

class ConfigChoices:
    dtype = ["Numeric", "AlphaNumeric", "Decimal"]
    subtype = ["int","float","string"]
    rangetype = {"AlphaNumeric":["predefined","FROM-LIST","CHAR-FROM-LIST"], "Decimal":["START-END", "FROM-LIST"], "Numeric":["START-END", "FROM-LIST"] }
    range = {"predefined":["ALL ALPHABETS","LOWERCASE ALPHABETS","UPPERCASE ALPHABETS"], "CHAR-FROM-LIST":["A","B","c","d","x","y","z"],"FROM-LIST":["AA","BB","CC","DD"]}
    NUM_COLS = 200


def generate_simple_config():
    # generate set of simple configs (name, type, range)
    rng = SimpleRandomGenerator()
    jsonList = {"name": "Sample Column 1", "type": "numeric", "subtype": "int", "minLen": "5", "maxLen": "20", "rangeType": "start-end", "range": [-10000,10000], "variance": "ignore", "colPosn": "ignore", "unique": "ignore", "dupFactor": "ignore", "relation": "ignore", "template": "ignore", "custom": "ignore"}
    configlist=[]

    for i in range(ConfigChoices.NUM_COLS):
        listele = jsonList
        dtype = rng.element_from_list(ConfigChoices.dtype)
        subtype = "float" if dtype.upper()=="DECIMAL" else ""
        rangetype = rng.element_from_list(ConfigChoices.rangetype[dtype])
        
        if rangetype == "predefined":
            range = rng.element_from_list(ConfigChoices.range[rangetype]) 
        elif rangetype == "CHAR-FROM-LIST" or rangetype == "FROM-LIST": 
            range = ConfigChoices.range[rangetype]
        else:
            range = jsonList["range"]

        listele["name"] = f"Sample Column {i+1}" 
        listele["type"] = dtype
        listele["subtype"] = subtype
        listele["rangeType"] = rangetype
        listele["range"] = range

        # print(listele)
        configlist.append(listele)


    json.dump(configlist, open("testing_configs/simplecols200.json","w+"))


samplelist = json.load(open("testing_configs/simplecols200.json","r"))
for i in samplelist:
    print(i)