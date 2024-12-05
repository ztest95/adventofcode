class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = []

    def next_data(self):
        return [node.data for node in self.next]

def topological_sort(node: Node, visited: set, stack: list[Node]):
    visited.add(node)
    for next_node in node.next:
        if next_node not in visited:
            topological_sort(next_node, visited, stack)
    stack.append(node)
    
    return stack

def add_next(node_a, node_b):
    
    for node in node_a.next:
        if node.data == node_b.data:
            return 
        
    node_a.next.append(node_b)

def solve_star_1(input: list[str]) -> int:
    res = 0

    sec1_end_idx = 0
    start_nodes = [] # cant use set since i need to get 
    nums = set()
    rules = []
    for line_index in range(len(input)):
        level_2 = set()
        if input[line_index] == '':
            sec1_end_idx = line_index
            break
        input[line_index]
        a, b = input[line_index].split('|')
        rules.append((a, b))
        nums.add(a)
        nums.add(b)
    
    nums = list(nums)
    for num in nums:
        start_nodes.append(Node(num))

    mapp = dict(zip(nums, start_nodes))
    for rule in rules:
        a = rule[0]
        b = rule[1]
        node_a = mapp[a]
        node_b = mapp[b]
        add_next(node_a, node_b)

    sec2 = input[sec1_end_idx+1:]
    
    upds = []
    for line in sec2:
        upds.append(line.split(','))
    
    
    for upd in upds:
        fail = False
        print("====LINE: ", upd)
        aa = []
        for page in upd:
            copy = upd.copy()
            if page in nums:
                aa.append(page)
                after = list[set(mapp[page].next_data()) - set(copy)]
                print('visited', aa)

        for i in range(len(aa)-1, 0, -1):
            before = set(aa[:i])
            for ele in mapp[aa[i]].next_data():
                if ele in before:
                    fail = True
                    break
        
        if not fail:
            res += int(aa[int(len(aa)/2)])

    return res

def solve_star_2(input: list[str]) -> int:
    res = 0
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))

