from SimpleColConfig import SimpleColConfig
from Constants import Constants

config1=SimpleColConfig(noofrows=Constants.NUM_ROWS.value)
config1.construct_generator()
# print(Constants.NUM_ROWS.value)