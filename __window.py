# In the name of Allah

from cmath import e
from .__types import NameType, Keys


class TmuxWindow:
    def __init__(self, session: 'TmuxSession', name: NameType, index: int) -> None:
        self.__parent = session
        self.__name = name
        self.__stream = []
        self.__index = index

    def session(self, name: str) -> 'TmuxSession':
        return self.__parent.session(name)

    def window(self, name: NameType) -> 'TmuxWindow':
        return self.__parent.window(name)

    @property
    def name(self) -> NameType:
        return self.__name

    def write(self, string: str) -> 'TmuxWindow':
        self.__stream.append(string)
        return self

    @property
    def enter(self) -> 'TmuxWindow':
        self.__stream.append(Keys.Enter)
        return self

    def command(self, string: str) -> 'TmuxWindow':
        """Note: This method is just like using '.write(string).enter'"""
        return self.write(string).enter

    @property
    def shell(self) -> str:
        # A simple comment line
        if self.__name != None:
            s = f'# {self.__name}'
        else:
            s = '#'

        # Create the window or rename it!
        if self.__index > 0:
            s += f'\ntmux new-window -t "{self.__parent.name}":{self.__index}'
            if self.__name != None:
                s += f' -n "{self.__name}"'
        else:
            if self.__name != None:
                s += f'\ntmux rename-window {self.__name}'

        # Commands
        s += '\ntmux send-keys'
        for item in self.__stream:
            if type(item) == str:
                s += f" '{item}'"
            elif item == Keys.Enter:
                s += ' ENTER'

        return s
