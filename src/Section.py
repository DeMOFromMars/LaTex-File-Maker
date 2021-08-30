# File: Section
# Version 1.2
# By Devin
# Last Modifed 30/8/21

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


def Get_Level_Str(level) -> str:
    levels = {
        Level.PART: "part",
        Level.CHAPTER: "chapter",
        Level.SECTION: "section",
        Level.SUBSECTION: "subsection",
        Level.SUBSUBSECTION: "subsubsection",
        level.PARAGRAPH: "paragraph",
        level.SUBPARAGRAPH: "subparagraph"
    }
    return levels.get(level)


class Section(Command):
    """Section """

    def __init__(self, _title: str, level=Level.SECTION):
        super().__init__(Get_Level_Str(level), mod=[], params=[_title])


    def __str__(self):
        return "\\" + self.getName() + "{" + self.getParams()[0] + "}"
