from tree import Tree


class Parser:

    @staticmethod
    def tokenize(string):
        return string.replace('(', ' ( ').replace(')', ' ) ').split()

    @classmethod
    def parse(cls, string):
        return cls.build_tree(cls.tokenize(string))

    @classmethod
    def build_tree(cls, tokens):
        if len(tokens) == 0:
            raise SyntaxError('Unexpected EOL')

        token = tokens.pop(0)
        if token == '(':
            new_node = Tree(tokens.pop(0))
            while tokens[0] != ')':
                new_node.add_children(cls.build_tree(tokens))
            tokens.pop(0)    # pop off ')'
            return new_node

        elif token == ')':
            raise SyntaxError('Unexpected ")"')
        return Tree(token)
