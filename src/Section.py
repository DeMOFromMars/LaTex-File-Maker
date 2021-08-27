# File: Section
# Version 1.5
# By Devin O'Brien
# Last Modifed 27/8/21

import enum
from src.Command import Command
class Level(enum.Enum):
    PART = -1
    CHAPTER = 0
    SECTION = 1
    SUBSECTION = 2
    SUBSUBSECTION = 3
    PARAGRAPH = 4
    SUBPARAGRAPH = 5
def Get_Level_Str( level)->str:
    levels = {
    Level.PART:"part",
    Level.CHAPTER:"chapter",
    Level.SECTION:"section",
    Level.SUBSECTION:"subsection",
    Level.SUBSUBSECTION:"subsubsection",
    level.PARAGRAPH:"paragraph",
    level.SUBPARAGRAPH:"subparagraph"
    }
    return levels.get(level)
@Command
class Section:
    """Section """
    __title = None
    __level  = None
    def __init__(self,_title:str, level=Level.SECTION):
        super.__init__(Get_Level_Str(level), params=[_title])

    def Get_Title(self):
        return self.__name

    def Set_Title(self, title):
        self.__name = title

    def Get_Level(self):
        return self.__level

    def Set_Level(self, level):
        if level < -1 or level > 5 or type(level) is not int:
            return False
        self.__level = level
        return True
      
    def __str__(self):
        return self.Get_Level_Str() + "{"+self.__title+"}"