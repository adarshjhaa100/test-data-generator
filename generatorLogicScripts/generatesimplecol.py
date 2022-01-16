import json
from simplerandomgenerator import SimpleRandomGenerator
from datetime import datetime
import time


class SimpleColConfig():
    
    def __init__(self, jsonconfig, noofrows) -> None:
        self.name = jsonconfig['name']
        self.type = jsonconfig['type']
        self.subtype = jsonconfig['subtype']
        self.minLen = int(jsonconfig['minLen'])
        self.maxLen = int(jsonconfig['maxLen'])
        self.rangeType = jsonconfig['rangeType']
        self.range = jsonconfig['range']
        self.variance = jsonconfig['variance']
        self.colPosn = jsonconfig['colPosn']
        self.unique = jsonconfig['unique']
        self.dupFactor = jsonconfig['dupFactor']
        self.relation = jsonconfig['relation']
        self.template = jsonconfig['template']
        self.custom = jsonconfig['custom']
        self.noofrows=int(noofrows)
        self.rng=SimpleRandomGenerator()

    def construct_generator(self):
        if(self.type.upper()=="NUMERIC"):
            print("numeric")
        if(self.type.upper()=="ALPHANUMERIC"):
            print("alphanumneric")    
            self.generatestring()
        if(self.type.upper()=="DECIMAL"):
            if(self.subtype=="FLOAT"):
                self.generatefloat()
                
    
    def generatestring(self):
        fromlist=[]
        if(self.rangeType.upper()=="PREDEFINED"):

            if(self.range.upper()=="ALL ALPHABETS"):
                fromlist=[chr(x) for x in range(65,91)]+[chr(x) for x in range(97,123)]    
            elif(self.range.upper()=="LOWERCASE ALPHABETS"):
                fromlist=[chr(x) for x in range(97,123)]
            elif(self.range.upper()=="UPPERCASE ALPHABETS"):
                fromlist=[chr(x) for x in range(65,91)]    
            else:
                print("Range not defined: ",{self.range})        
        
        columnValues=[self.name]
        for _ in range(self.noofrows):
            gen_string=self.rng.random_alphanum(self.minLen, self.maxLen, fromlist)
            columnValues.append(gen_string)

        # print(columnValues)
        with open(f"sampleoutput/generated_{int(time.time())}.csv","w+") as fw:
            writecounter=0
            for val in columnValues:
                fw.write(f"{val},\n")
                print(f"Written {writecounter} of {self.noofrows} values")
                writecounter+=1
            fw.close()

    def generatefloat(self):
        pass

    def generateinit(self):
        for k in self.jsonconfig:
            print("self."+k+" = "+"jsonconfig[\'"+k+"\']")



sampleconfig={}
with open("sampleconfigs/simpleconfig1.json","r") as fp:
    sampleconfig=json.load(fp)
    fp.close()


config1=SimpleColConfig(sampleconfig,5000)
config1.construct_generator()

# {"name": "Sample Column 1", "type": "AlphaNumeric", "subtype": "string", "minLen": "5", "maxLen": "20", "rangeType": "predefined", "range": "alphabets", "variance": "ignore", "colPosn": "ignore", "unique": "ignore", "dupFactor": "ignore", "relation": "ignore", "template": "ignore", "custom": "ignore"}