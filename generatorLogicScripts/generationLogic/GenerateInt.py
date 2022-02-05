import json

from generationLogic.simplerandomgenerator import SimpleRandomGenerator


class GenerateInt():
    def __init__(self) -> None:
        with open("generationConfig/generateInt.json","r") as f:
            self.functionMetaData = json.load(f)
        self.simpleRandomGenerator = SimpleRandomGenerator()
    def generate(self):
        fromlist, columnValues=[],[self.functionMetaData["name"]]
        if self.functionMetaData["rangeType"].upper()=="START-END":
            minval,maxval=self.functionMetaData["range"]["start"], self.functionMetaData["range"]["end"]
            print(minval,maxval)
            for _ in range(self.functionMetaData["noOfRows"]):
                columnValues.append(int(self.simpleRandomGenerator.generate_number(minval, maxval)))
        
        if self.functionMetaData["rangeType"].upper()=="FROM-LIST":
            fromlist=self.functionMetaData["range"]
            for _ in range(self.functionMetaData["noOfRows"]):
                gen_string=self.simpleRandomGenerator.elements_from_list(fromlist)
                columnValues.append(int(gen_string))
        return columnValues