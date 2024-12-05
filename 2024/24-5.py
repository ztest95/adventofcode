class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = []

def add_next(node_a, node_b):
    
    for node in node_a.next:
        if node.data == node_b.data:
            return 
        
    node_a.next.add(node_b)

# def solve_star_1(input: list[str]) -> int:
#     res = 0

#     sec1_end_idx = 0
#     start_nodes = [] # cant use set since i need to get 
#     for line_index in range(len(input)):
#         if input[line_index] == '':
#             sec1_end_idx = line_index
#             break
#         input[line_index]
#         a, b = input[line_index].split('|')
#         node_a = Node(a)
#         node_b = Node(b)
#         for node in start_nodes:
#             if node.data == a: # if node already in list, add node b as next
#                 node.next.append(node_b)
#                 break
        
#         # if node not in list, add node a and b
#         else:
#             node_a.next.append(node_b)
#             start_nodes.append(node_a)

    
#     # for node in start_nodes:
#     #     print(node.data)
#     #     print(node.next)

#     sec2 = input[sec1_end_idx+1:]

#     print(start_nodes)
#     complete_rules = []
#     for node in start_nodes:
#         complete_rules.append(node.data)
#         for next_node in node.next:
#             complete_rules.append(next_node.data)

#     cr_set = set()
#     for i in range(len(complete_rules)):
#         if complete_rules[i] in cr_set:
#             complete_rules[i] = ''
#         else:
#             cr_set.add(complete_rules[i])
    
#     iter_n = len(complete_rules) - len(cr_set)

#     while iter_n > 0:
#         complete_rules.remove('')
#         iter_n -= 1
        

#     # for line_index in range(len(sec2)):
#     #     pages_lst = sec2[line_index].split(',')
        
#     #     for p_num in pages_lst:

            
#     #         for node in start_nodes:
#     #             if node.data == p_num:
#     #                 break
#     #         else:
#     #             node = Node(p_num)
#     #             start_nodes.append(node)

    # return res

def solve_star_1(input: list[str]) -> int:
    res = 0

    return res

def solve_star_2(input: list[str]) -> int:
    res = 0
    return res

if __name__ == "__main__":

    with open('2024/testinput.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))

