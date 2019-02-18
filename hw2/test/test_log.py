import pytest
import logging
from analyzer import log as lg


@pytest.fixture()
def resource_setup():
    logger = lg.Log('test_log', 'test_log.txt')
    return logger


@pytest.mark.parametrize('value', ['INFO', 'DEBUG', 'ERROR'])
def test_logger_set_level(resource_setup, value):
    log = resource_setup
    log.setLevel(value)
    assert logging.getLevelName(log.my_log.level) == value


@pytest.mark.parametrize('msg', [('%(message)s'), None])
def test_logger_formatter_func(resource_setup, msg):
    log = resource_setup
    log.setLevel('DEBUG')
    log.formatter_func(msg)
    if msg is None:
        msg = log.default_formatter
    assert log.formatter._fmt == msg


def test_logger_add_console_handler_false():
    log = lg.Log(name='test_log_h_false', console=False)
    log.add_console_handler(console=False)
    handlers = log.my_log.handlers[:]
    assert '<StreamHandler <stderr> (NOTSET)>' not in str(handlers)


def test_logger_add_console_handler_true():
    log = lg.Log(name='test_log_h_true', console=False)
    log.add_console_handler(console=True)
    handlers = log.my_log.handlers[:]
    assert '<StreamHandler <stderr> (NOTSET)>' in str(handlers)


def test_logger_add_file_handler_true():
    f_name = 'test_log_f_true.txt'
    log = lg.Log(name='test_log_f_true', console=False)
    log.add_file_handler(f_name=f_name)
    handlers = log.my_log.handlers[:]
    assert '<FileHandler' in str(handlers)
    assert f_name in str(handlers)

def test_logger_add_file_handler_false():
    log = lg.Log(name='test_log_f_false', console=False)
    log.add_file_handler()
    handlers = log.my_log.handlers[:]
    assert '<FileHandler' not in str(handlers)