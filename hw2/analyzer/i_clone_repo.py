from abc import ABCMeta, abstractmethod

class iCloneRepo():
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self):
        '''Clone repository'''


