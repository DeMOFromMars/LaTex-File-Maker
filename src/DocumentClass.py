# File: DocumentClass
# Version 1.5
# By Devin O'Brien
# Last Modified 26/8/21

import Command
class DocumentClass(Command):
	def __init__(self, doc, mod = []):
		super().__init__("documentclass", mod, doc)

		