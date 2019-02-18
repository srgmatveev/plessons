from abc import ABCMeta, abstractmethod


class iReport():
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self):
        '''Save report'''
