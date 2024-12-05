class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = []

    def next_data(self):
        return [str(node.data) for node in self.next]

def add_next(node_a, node_b):
    # this is just like adding element to a set
    # does not allow duplicates
    for node in node_a.next:
        if node.data == node_b.data:
            return 
        
    node_a.next.append(node_b)

def solve_star_1(input: list[str]) -> int:
    # Idea is to get nodes.next for each node from right to left on update
    # if an element in node.next is in the before list, then fail
    
    res = 0

    sec1_end_idx = 0
    start_nodes = [] 
    nums = set()
    rules = []
    for line_index in range(len(input)):
        if input[line_index] == '':
            sec1_end_idx = line_index
            break
        
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

    # convert each list of updates to a list of lists
    upds = []
    for line in sec2:
        upds.append(line.split(','))
    
    for upd in upds: # for each update
        fail = False
        aa = upd
        for i in range(len(aa)-1, 0, -1): # iterate from the end
            before = set(aa[:i]) 
            for ele in mapp[aa[i]].next_data(): 
                if ele in before: # if node.next is in before[]
                    fail = True # fail
                    break
        
        if not fail:
            res += int(aa[int(len(aa)/2)])

    return res

def solve_star_2(input: list[str]) -> int:
    # my initial idea was that, i could create a list of all the values that follows all the rules...
    # iterating through that list and appending whenever the val exists in updates resulting in the ordered_update.
    #   all_vals_sorted = [] 
    #   ordered_update = []
    #   for ele in all_vals_sorted: # iterate universally sorted graph
    #   if ele in update: # for each ele, check if its in an update
    #   ordered_update.append(ele) # add new (ordered) list
    # this worked on the test input which has like 5 pages each update, but not on actual input. 
    # took me so much time to debug and try a diff approach 
    
    res = 0

    sec1_end_idx = 0
    start_nodes = [] 
    nums = set()
    rules = [] # list of rules "Before|After"
    for line_index in range(len(input)):
        if input[line_index] == '':
            sec1_end_idx = line_index # indicate start of next section
            break # stop at the end of first section
        
        input[line_index]
        a, b = input[line_index].split('|')
        rules.append((a, b))
        nums.add(a)
        nums.add(b)
    
    # Create list for each number
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

    # List for each update
    upds = []
    for line in input[sec1_end_idx+1:]:
        upds.append(line.split(','))

    indeg_count = {node: 0 for node in start_nodes}
    for node in start_nodes:
        for next_node in node.next:
            indeg_count[next_node] += 1

    zero_indeg = [node for node in start_nodes if indeg_count[node] == 1]

    def topo_sort(S: list[Node], l: list[Node] = None) -> list:
        if l is None:
            l = []
        if not S:
            return l
        v = S.pop()
        l.append(v)
        for w in v.next:
            indeg_count[w] -= 1
            if indeg_count[w] == 0:
                S.append(w)

        return topo_sort(S, l)
    
    def sort(S: list[Node]) -> list:
        while True:
            is_sorted = True
            i = 0
            while i < len(S) - 1:
                if (S[i+1], S[i]) in rules:
                    is_sorted = False
                    S[i], S[i+1] = S[i+1], S[i]
                i += 1  # Increment i in each iteration
            
            if is_sorted:
                return S
            
    final_seq = topo_sort(zero_indeg)
    final_seq = sort(start_nodes)

    for upd in upds:
        ordered = []
        ordered = sort(upd.copy())

        if ordered != upd:
            res += int(ordered[len(ordered)//2]) 
    
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))
