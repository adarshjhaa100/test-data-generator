import importlib
import json
import os
import time

from Constants import Constants, OutputFormat

class SimpleColGenerator():
    def __init__(   
                    self,
                    name,
                    outputFormat
                ) -> None:
        self.name = name
        self.outputFormat = outputFormat
    
    def generate_col(self):
        module = importlib.import_module(Constants.GENERATION_LOGIC_PATH.value + self.name)
        my_class = getattr(module, self.name)
        my_instance = my_class()
        if self.outputFormat == OutputFormat.LIST:
            return my_instance.generate()
        elif self.outputFormat == OutputFormat.CSV:
            col = my_instance.generate()
            self.generate_csv(col)      
        elif self.outputFormat == OutputFormat.JSON:
            col = my_instance.generate()
            self.generate_json(col)
    
    def generate_csv(self,col):
        filename = f"sampleoutput/csv/generated_{int(time.time_ns())}.{OutputFormat.CSV.value}"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename,"w+") as f:
            writecounter = 0
            for val in col:
                f.write(f"{val},\n")
                print(f"Written {writecounter} of {len(col)} values")
                writecounter += 1
        print(f"Written to: '{filename}'")
    
    def generate_json(self,col):
        col_dict = {col[0]:col[1:]}
        filename = f"sampleoutput/json/generated_{int(time.time_ns())}.{OutputFormat.JSON.value}"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename,"w+") as f:
            col_dict_json_val = json.dumps(col_dict)
            f.write(col_dict_json_val)
        print(f"Written to: '{filename}'")
            