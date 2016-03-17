import sys

DEBUG = True

class Record:
    def __init__(self, line):
        line = line.strip().split('\t')
        self.index = line[0]
        self.word = line[1]
        self.head = line[6]
        self.type = line[7]
        self.children = []
        self.parent = None
        self.weight = None

    def calculate_weight(self):
        if len(self.children) == 0:
            self.weight = 1
        else:
            self.weight = 1
            for child in self.children:
                self.weight += child.calculate_weight()
        return self.weight

    def pruning(self):
        for child in self.children:
            if (child._pruning_that() or child._pruning_wh()):
                self.children.remove(child)
            child.pruning()

    def _pruning_wh(self):
        remove = ['who', 'where', 'when', 'which']
        return self.word in remove

    def _pruning_that(self):
        return self.word == 'that' and self.weight >= 5

    def generate_sentence(self):
        all_nodes = self.get_all_nodes()
        all_nodes = sorted(all_nodes, key=lambda x:int(x.index))
        return ' '.join([x.word for x in all_nodes])

    def get_all_nodes(self):
        result = [self]
        for child in self.children:
            result += child.get_all_nodes()
        return result

    def print_tree(self, depth=0):
        print '\t'*depth, self.word, self.type
        for child in self.children:
            child.print_tree(depth + 1)

def read_data(source):
    records = []
    # output_depth = sys.argv[1] if len(sys.argv) != 1 else -1
    for line in source:
        if len(line) == 1:
            continue
        node = Record(line)
        records.append(node)

    # result = tree_print(output_depth, ["0"], records)

    head = build_dependency_tree(records)
    head.calculate_weight()
    if DEBUG: head.print_tree()
    head.pruning()
    if DEBUG: head.print_tree()
    return head.generate_sentence()


def main():
    print read_data(sys.stdin)

def build_dependency_tree(records, head=None):
    if head == None:
        for node in records:
            if node.head == "0":
                head = node
                break
    if head == None:
        return None
    for node in records:
        if node.head == head.index:
            head.children.append(node)
    for node in head.children:
        build_dependency_tree(records, node)
    return head

def tree_print(depth, node_list, records):
    if len(node_list) == len(records):
        return []
    next_node_list = []
    result = []
    sentence = ""
    for r in records:
        if r.head in node_list or r.index in node_list:
            sentence += r.word + " "
            next_node_list.append(r.index)
    result.append(sentence)
    result = result + tree_print(depth - 1, next_node_list, records)
    return result

if __name__ == '__main__':
    main()
