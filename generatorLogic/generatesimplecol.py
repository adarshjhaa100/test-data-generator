import json
from rngs.simplerandomgenerator import SimpleRandomGenerator
from datetime import datetime
import time

NUM_ROWS=20000

class SimpleColConfig():
    ''' Class to generate "simple" columns (with type and reange defined) '''
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
        self.precision=5 # TODO: need to add field for this
        self.rng=SimpleRandomGenerator()

    def construct_generator(self):
        ''' calls other function according to type and subtype specified'''
        print(self.type, self.subtype)
        if(self.type.upper()=="NUMERIC"):
            print("numeric")
            self.generateint()
        if(self.type.upper()=="ALPHANUMERIC"):
            print("alphanumneric")    
            self.generatestring()
        if(self.type.upper()=="DECIMAL"):
            if(self.subtype.upper()=="FLOAT"):
                print("FLOAT")
                self.generatefloat()             
    

    def generatestring(self):
        ''' Generate string from a set of predefined strings or a given character list'''
        fromlist, columnValues=[],[self.name]
        
        if(self.rangeType.upper()=="PREDEFINED"):

            if(self.range.upper()=="ALL ALPHABETS"):
                fromlist=[chr(x) for x in range(65,91)]+[chr(x) for x in range(97,123)]    
            elif(self.range.upper()=="LOWERCASE ALPHABETS"):
                fromlist=[chr(x) for x in range(97,123)]
            elif(self.range.upper()=="UPPERCASE ALPHABETS"):
                fromlist=[chr(x) for x in range(65,91)]    
            else:
                print("Range not defined: ",{self.range})        
        
            for _ in range(self.noofrows):
                gen_string=self.rng.random_alphanum(self.minLen, self.maxLen, fromlist)
                columnValues.append(gen_string)

        if self.rangeType.upper()=="FROM-LIST":
            fromlist=self.range
            for _ in range(self.noofrows):
                gen_string=self.rng.element_from_list(fromlist)
                columnValues.append(gen_string)

        if self.rangeType.upper()=="CHAR-FROM-LIST":
            fromlist=self.range
            for _ in range(self.noofrows):
                gen_string=self.rng.random_alphanum(self.minLen, self.maxLen, fromlist)
                columnValues.append(gen_string)

        self.savetofile(columnValues,"csv")
            
        
    def generatefloat(self):
        ''' Generate floats given range or list alongwith precision '''
        fromlist, columnValues=[],[self.name]
        if self.rangeType.upper()=="START-END":
           
            minval,maxval=float(self.range[0]), float(self.range[1])
            print("start-end", minval, maxval)
            for _ in range(self.noofrows):
                columnValues.append(float(self.rng.generate_float(minval,maxval,self.precision)))
        
        if self.rangeType.upper()=="FROM-LIST":
            fromlist=self.range
            for _ in range(self.noofrows):
                gen_string=self.rng.element_from_list(fromlist)
                columnValues.append(float(gen_string))

        self.savetofile(columnValues,"csv")    

    def generateint(self):
        ''' generate integers within range or from a list '''
        fromlist, columnValues=[],[self.name]
        if self.rangeType.upper()=="START-END":
            minval,maxval=int(self.range[0]), int(self.range[1])
            for _ in range(self.noofrows):
                columnValues.append(int(self.rng.generate_number(minval, maxval)))
        
        if self.rangeType.upper()=="FROM-LIST":
            fromlist=self.range
            for _ in range(self.noofrows):
                gen_string=self.rng.element_from_list(fromlist)
                columnValues.append(int(gen_string))

        self.savetofile(columnValues,"csv")


    def generateinit(self):
        ''' Igonre this for now '''
        for k in self.jsonconfig:
            print("self."+k+" = "+"jsonconfig[\'"+k+"\']")

    def savetofile(self, columnValuesSet, fileextension="csv"):
        # print(columnValues)
        filename = f"sampleoutput/generated_{int(time.time_ns())}.{fileextension}"
        with open(filename,"w+") as fw:
            writecounter=0
            for val in columnValuesSet:
                fw.write(f"{val},\n")
                print(f"Written {writecounter} of {self.noofrows} values")
                writecounter+=1
            fw.close()
        print(f"Written to: '{filename}'")


# load from sampleconfig file
sampleconfig={}
with open("sampleconfigs/singlecolconfig1.json","r") as fp:
    sampleconfig=json.load(fp)
    fp.close()

# generate config file
print(sampleconfig)
config1=SimpleColConfig(sampleconfig,NUM_ROWS)
config1.construct_generator()

# {"name": "Sample Column 1", "type": "AlphaNumeric", "subtype": "string", "minLen": "5", "maxLen": "20", "rangeType": "predefined", "range": "alphabets", "variance": "ignore", "colPosn": "ignore", "unique": "ignore", "dupFactor": "ignore", "relation": "ignore", "template": "ignore", "custom": "ignore"}