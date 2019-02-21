from abc import ABCMeta, abstractmethod


class iReport():
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self):
        '''Save report'''


def reporter(report=None):
    if report is not None:
        report.save()