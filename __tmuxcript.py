# In the name of Allah

from .__session import TmuxSession

class Tmuxcript:
    def __init__(self) -> None:
        self.__sessions = {}
    
    def session(self, name: str) -> TmuxSession:
        if name in self.__sessions:
            raise Exception('This session already exists. Use [] operator to fetch it.')
        sess = TmuxSession(self, name)
        self.__sessions[name] = sess
        return sess
    
    def __getitem__(self, kw) -> TmuxSession:
        return self.__sessions[kw]
    
    @property
    def shell(self) -> str:
        s = """#!/bin/sh
#
# ---------------------------------------------------------------------
# Hi,
# 
# This shell script is made by tmuxcript.
# https://github.com/ADanayi/tmuxcript
# 
# Please report any issues/suggestions/problems to adanayidet@gmail.com
# 
# Bests,
# Abolfazl Danayi
# ---------------------------------------------------------------------"""

        for session in self.__sessions.values():
            s += f'\n\n{session.shell}'
        
        return s

    def save(self, filepath: str):
        with open(filepath, 'w') as file:
            file.write(self.shell)
