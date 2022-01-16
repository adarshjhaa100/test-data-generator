import json
from simplerandomgenerator import SimpleRandomGenerator



class SimpleColConfig():
    
    def __init__(self, jsonconfig, noofrows) -> None:
        self.name = jsonconfig['name']
        self.type = jsonconfig['type']
        self.subtype = jsonconfig['subtype']
        self.minLen = jsonconfig['minLen']
        self.maxLen = jsonconfig['maxLen']
        self.rangeType = jsonconfig['rangeType']
        self.range = jsonconfig['range']
        self.variance = jsonconfig['variance']
        self.colPosn = jsonconfig['colPosn']
        self.unique = jsonconfig['unique']
        self.dupFactor = jsonconfig['dupFactor']
        self.relation = jsonconfig['relation']
        self.template = jsonconfig['template']
        self.custom = jsonconfig['custom']
        self.noofrows=noofrows
        self.rng=SimpleRandomGenerator()

    def construct_generator(self):
        if(self.type.upper()=="NUMERIC"):
            print("numeric")
        if(self.type.upper()=="ALPHANUMERIC"):
            print("alphanumneric")    
        if(self.type.upper()=="DECIMAL"):    
            print("decimal")
        for i in range(self.noofrows):
            print(self.rng.generate_float(-2354235,425435,6))

    def generateinit(self):
        for k in self.jsonconfig:
            print("self."+k+" = "+"jsonconfig[\'"+k+"\']")


sampleconfig={}
with open("sampleconfigs/simpleconfig1.json","r") as fp:
    sampleconfig=json.load(fp)
    fp.close()


config1=SimpleColConfig(sampleconfig,44)
config1.construct_generator()

# {"name": "Sample Column 1", "type": "AlphaNumeric", "subtype": "string", "minLen": "5", "maxLen": "20", "rangeType": "predefined", "range": "alphabets", "variance": "ignore", "colPosn": "ignore", "unique": "ignore", "dupFactor": "ignore", "relation": "ignore", "template": "ignore", "custom": "ignore"}