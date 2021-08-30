# File: Command
# Version 1.2
# By Devin
# Last Modified 30/8/21

class Command:
    __name = None
    __mod = []
    __params = []

    def __init__(self, name, mod=[], params=[]):
        self.__name = name
        if mod is None:
            mod = []
        self.__mod = mod
        self.__params = params

    def getName(self):
        return self.__name
    def getParams(self):
        return self.__params
    def __str__(self):
        out = "\\"
        out = out + self.__name
        if len(self.__mod) > 0:
            out = out + '['
            counter = 0
            for m in self.__mod:
                out = out + str(m)
                if len(self.__mod) -1 != counter:
                    out = out + ', '
            out = out + ']'
        if len(self.__params) > 0:
            for param in self.__params:
                out = out + "{" + str(param) + "}"
        return out
