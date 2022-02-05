# For testing new generation Logic
from generationLogic.GenerateInt import GenerateInt
from SimpleColGenerator import SimpleColGenerator
from Constants import OutputFormat

generatingInt = SimpleColGenerator("GenerateInt",OutputFormat.CSV)
print(generatingInt.generate_col())