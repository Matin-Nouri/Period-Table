import json as JsonParser
from os import name
class Atom:
    def __init__(self,x):
        self.symbol=""
        self.number=0
        if name=='posix':
            self.path = './data/'
        else:
            self.path = '.\\data\\'
        if type(x) is str:
            self.symbol = x
        elif type(x) is int:
            self.number = x
        with open(f"{self.path}PeriodicTableJSON.json",'r+') as file:
            self.JsonParser = file.read()
            file.close()
        self.data = JsonParser.loads(self.JsonParser)
    def Get_Data(self):
        data = self.data
        data = data['elements']
        for i in data:
            if self.symbol != "":
                # it is symbol
                if i['symbol'] == self.symbol:
                    return i
            elif self.number != 0:
                #it is number
                if i['number'] == self.number:
                    return i
        