import ast

tree = ast.parse('''
fruits = ['grapes', 'mango']
name = 'peter'
def aaa():
    rrr=15
    www=28
    def bbb():
        ttt=45
    ttt1=456
for fruit in fruits:
    print('{} likes {}'.format(name, fruit))
''')

print(ast.dump(tree))

class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self, tree_node):
        print('{}'.format(tree_node.s))


class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str('String: ' + tree_node.s)

NodeTransformer().visit(tree)
NodeVisitor().visit(tree)

tree_node = ast.fix_missing_locations(tree)
exec(compile(tree_node, '', 'exec'))
iter_children = ast.iter_child_nodes(tree_node)
for node in iter_children:
    if isinstance(node, ast.FunctionDef):
        for node1 in ast.walk(node):
            if isinstance(node1, ast.Name):
                print(node1.id)
def aaa(ttt='ddd'):
    print(f'{ttt}')

def bbb(aaa=None, eee ="helloid"):
    aaa(ttt=eee)
bbb(aaa=aaa, eee='USSR')