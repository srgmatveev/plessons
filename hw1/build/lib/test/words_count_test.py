import pytest
import os
from wordscount import words_count as wc

path = './projects/django/'


def test_make_flat_list():
    assert wc.make_flat_list([(1, 2), (3, 4)]) == [1, 2, 3, 4]


def test_is_verb_true():
    assert wc.is_verb('do') == True


def test_is_verb_false():
    assert wc.is_verb('punch') == False


def test_get_file_names():
    filenames = ['./projects/django/__init__.py',
                 './projects/django/first.py']
    assert wc.get_file_names(path).sort() == filenames.sort()


def test_all_function_names():
    filenames = wc.get_file_names(path)
    print(filenames)
    trees = wc.get_syntax_trees(filenames)
    assert wc.get_all_functions_names(trees) == ['obtain', 'get', 'do', 'get']


def test_remove_functions_names_with_danders_from_list():
    assert wc.remove_functions_names_with_danders_from_list(
        ['obtain', 'get', '__aaa__','do', 'get']) == ['obtain', 'get', 'do', 'get']
