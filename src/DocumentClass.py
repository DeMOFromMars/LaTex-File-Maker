# File: DocumentClass
# Version 1.5
# By Devin O'Brien
# Last Modified 26/8/21
from src.Command import Command


class DocumentClass(Command):
    def __init__(self, doc:str, mod=[]):
        super().__init__("documentclass", mod, [doc])
