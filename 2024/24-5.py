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
    # sort each update based on rules

    res = 0

    sec1_end_idx = 0
    rules = [] # list of rules "Before|After"
    for line_index in range(len(input)):
        if input[line_index] == '':
            sec1_end_idx = line_index # indicate start of next section
            break # stop at the end of first section
        
        input[line_index]
        a, b = input[line_index].split('|')
        rules.append((a, b))

    # List for each update
    upds = []
    for line in input[sec1_end_idx+1:]:
        upds.append(line.split(','))
    
    def sort(S: list[Node]) -> list:
        while True:
            is_sorted = True # assume sorted
            i = 0
            while i < len(S) - 1:
                if (S[i+1], S[i]) in rules: # if flipped
                    is_sorted = False # not sorted
                    S[i], S[i+1] = S[i+1], S[i] # and swap
                i += 1  
            
            if is_sorted:
                return S

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
