class Tree:
    # prefixes
    root = "+--"
    base = " "
    branch = "|   "
    last_child = "    "

    def __init__(self, content):
        self.content = content
        self.children = []

    def add_children(self, child):
        self.children.append(child)

    def build_components(self, is_root=False, is_last=False, prefix="", components=None):
        if not is_root:
            components.append(prefix)
            components.append(self.root)
        components.append(self.content)
        components.append("\n")

        prefix = self.update_prefix(prefix, is_root, is_last)

        child_count = len(self.children)
        for i, child in enumerate(self.children):
            # we do not draw the line to the last child
            if i == child_count-1:
                child.build_components(is_last=True, prefix=prefix, components=components)
            else:
                child.build_components(prefix=prefix, components=components)

    def update_prefix(self, cur_prefix, is_root, is_last):
        if is_root:
            prefix = self.base
        elif is_last:
            prefix = cur_prefix + self.last_child
        else:
            prefix = cur_prefix + self.branch
        return prefix

    def to_string(self):
        components = []
        self.build_components(is_root=True, components=components)
        return ''.join(components)

    def print(self):
        print(self.to_string())

    def __str__(self):
        return self.to_string()
