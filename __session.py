# In the name of Allah

from .__window import TmuxWindow
from .__types import NameType


class TmuxSession:
    def __init__(self, parent: 'Tmuxcript', name: str) -> None:
        """Enter session name. It is required."""
        if type(name) != str or len(name) == 0:
            raise Exception('Bad session name: {}'.format(name))
        self.__name = name
        self.__windows = []
        self.__parent = parent

    def session(self, name: str) -> 'TmuxSession':
        return self.__parent.session(name)

    def window(self, name: NameType) -> TmuxWindow:
        """Enter the window's name. If you don't enter the name,
TMUX will automatically generate a number-name, which is not recommended."""
        window = TmuxWindow(self, name, len(self))
        self.__windows.append(window)
        return window

    def __getitem__(self, kw: str) -> TmuxWindow:
        for window in self.__windows:
            if window.name == kw:
                return window
        raise Exception('Window not existing')

    def __len__(self) -> int:
        return len(self.__windows)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def shell(self) -> str:
        # A simple comment line
        s = '#######################'
        s += f'\n# {self.__name}'

        # Create the session
        s += f'\ntmux new-session -d -s "{self.__name}"'

        for window in self.__windows:
            s += f'\n\n{window.shell}'

        return s
