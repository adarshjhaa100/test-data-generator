import enum

class Constants(enum.Enum):
    NUM_ROWS = 20
    GENERATION_LOGIC_PATH = 'generationLogic.'

class OutputFormat(enum.Enum):
    CSV = "csv"
    JSON = "json"
    LIST = "list"
