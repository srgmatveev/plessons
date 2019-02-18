import logging


class Log(object):
    default_formatter = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def __init__(self, name=None, f_name=None, format_str=None, console=True):
        self.my_log = logging.getLogger(name)
        self.setLevel()
        self.formatter_func(msg=format_str)
        self.add_console_handler(console=console)
        self.add_file_handler(f_name=f_name)

    def setLevel(self, level='INFO'):
        self.my_log.setLevel(level)
        return self

    def formatter_func(self, msg=None):
        if msg is None:
            self.formatter = logging.Formatter(
                self.default_formatter)
        else:
            self.formatter = logging.Formatter(msg)
        return self

    def add_console_handler(self, console=True):
        if console:
            handler = logging.StreamHandler()
            handler.setFormatter(self.formatter)
            self.my_log.addHandler(handler)

    def add_file_handler(self, f_name=None):
        if f_name is not None:
            fh = logging.FileHandler(f_name)
            fh.setFormatter(self.formatter)
            self.my_log.addHandler(fh)

    def critical(self, msg, *args, **kwargs):
        self.my_log.critical(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.my_log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.my_log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.my_log.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.my_log.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.my_log.exception(msg, *args, exc_info=True, ** kwargs)


if __name__ == "__main__":
    first_logger = Log("hello", 'hello.txt')
    second_logger = Log("hello1", 'hello2.txt')
    first_logger.info("sss")
    second_logger.info('second')
