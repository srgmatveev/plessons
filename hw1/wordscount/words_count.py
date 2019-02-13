import nltk
import ast
import os
import collections

nltk.download('averaged_perceptron_tagger')


def make_flat_list(_list):
    ''' [(1,2), (3,4)] -> [1, 2, 3, 4]'''
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = nltk.pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_dir_file_names(files, dirname):
    filenames = []
    for file in files:
        if file.endswith('.py'):
            filenames.append(os.path.join(dirname, file))
            if len(filenames) == 100:
                break
    return filenames


def get_file_names(path):
    filenames = []
    for dirname, _, files in os.walk(path, topdown=True):
        filenames.append(get_dir_file_names(files, dirname))
    return make_flat_list(filenames)


def get_file_content(filename):
    with open(filename, 'r', encoding='utf-8') as open_file:
        return open_file.read()


def get_syntax_trees(filenames=[], with_filenames=False, with_file_content=False):
    trees = []
    for filename in filenames:
        file_content = get_file_content(filename)
        try:
            tree = ast.parse(file_content)
        except SyntaxError:
            continue

        if with_filenames:
            if with_file_content:
                trees.append((filename, file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)

    return trees


def get_all_function_names_for_tree(tree):
    return [node.name.lower() for node in ast.walk(tree) if isinstance(
        node, ast.FunctionDef)]


def get_all_functions_names(trees):
    functions = []
    for t in trees:
        functions.append(get_all_function_names_for_tree(t))
    return make_flat_list(functions)


def remove_functions_names_with_danders_from_list(_list):
    return [f for f in _list if not (f.startswith('__') and f.endswith('__'))]


def get_top_verbs_in_path(path, top_size=10):
    filenames = get_file_names(path)
    trees = get_syntax_trees(filenames)
    func_names = get_all_functions_names(trees)
    func_names = remove_functions_names_with_danders_from_list(func_names)
    verbs = get_flat_verbs_from_function_name(func_names)
    return collections.Counter(verbs).most_common(top_size)


def get_flat_verbs_from_function_name(func_names):
    verbs = []
    for function_name in func_names:
        verbs.append(get_verbs_from_function_name(function_name))
    return make_flat_list(verbs)


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


if __name__ == "__main__":
    wds = []
    projects = [
        'projects/django', ]
    ''' 'flask',
      'pyramid',
      'reddit',
      'requests',
      'sqlalchemy',
  
  ]
  '''
    for project in projects:
        path = os.path.join('.', project)
        get_top_verbs_in_path(path)
        wds += get_top_verbs_in_path(path)
    top_size = 200
    print('total {} words, {} unique'.format(len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)
