from analyzer.i_report import iReport
import collections

class ConsoleReport(iReport):
    def __init__(self, wds, top_size):
        self.wds = wds
        self.top_size = top_size

    def save(self):
        print('total {} words, {} unique'.format(len(self.wds), len(set(self.wds))))
        for word, occurence in collections.Counter(self.wds).most_common(self.top_size):
            print(word, occurence)
