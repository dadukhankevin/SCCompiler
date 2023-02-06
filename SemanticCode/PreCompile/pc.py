import re
import string
from bs4 import BeautifulSoup


# @key = api key
# @e = engine
# @/ = code
# @@ = comment
# @l = language

class PreCompiler:
    def __init__(self, text):
        self.text = text
        self.result = []
        self.api = None
        self.engine = ""
        self.comments = []
        self.lang = ""

    def process(self, line):
        if "@" == line[0]:
            line = line.split(" ")
            if "@key" == line[0] and self.api is None:
                self.api = line.replace("@key", "")
            elif "@e" == line[0] and self.engine is None:
                self.engine = line.replace("@e", "")
            elif "@\\" == line[0] and self.engine is None:
                self.result.append(" ".join(line))
        else:
            self.result.append(line)

    def precompile(self):
        lines = self.text.split("\n")
        for line in lines:
            self.process(line)
        return lines
