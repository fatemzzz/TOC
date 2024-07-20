from typing import List

class Tuple:
    def __init__(self, node1: str, trans: str, node2: str):
        self.node1 = node1
        self.trans = trans
        self.node2 = node2

tupleArrayList: List[Tuple] = []
stack: List[str] = []

def check_for_existing_tuple(tuple: Tuple):
    for tup in tupleArrayList:
        if tup.node1 == tuple.node1 and tup.node2 == tuple.node2:
            tup.trans = f"(({tup.trans})|({tuple.trans}))"
            return
    tupleArrayList.append(tuple)

def full_stack_with_nodes(number_of_middle_nodes: int):
    for i in range(number_of_middle_nodes):
        stack.append(str(i))

def remove_state():
    if len(stack) == 0:
        return
    Qrip = stack.pop()
    collar = search_for_collar(Qrip)
    left_tuples = divide_each_tuple(Qrip, True)
    right_tuples = divide_each_tuple(Qrip, False)
    for l_tuple in left_tuples:
        for r_tuple in right_tuples:
            tuple = Tuple(l_tuple.node1, f"({l_tuple.trans}){collar}({r_tuple.trans})", r_tuple.node2)
            tupleArrayList.append(tuple)
            union_added_tuples(tuple)
    remove_state()

def union_added_tuples(tuple: Tuple):
    removed_tuple = []
    for checking_tup in tupleArrayList:
        if checking_tup == tuple:
            continue
        if checking_tup.node1 == tuple.node1 and checking_tup.node2 == tuple.node2:
            tuple.trans = f"(({tuple.trans})|({checking_tup.trans}))"
            removed_tuple.append(checking_tup)
    for tup in removed_tuple:
        tupleArrayList.remove(tup)

def divide_each_tuple(Qrip: str, left: bool) -> List[Tuple]:
    tuples = []
    removed_tuples = []
    for tuple in tupleArrayList:
        if (tuple.node2 == Qrip and left) or (tuple.node1 == Qrip and not left):
            removed_tuples.append(tuple)
            tuples.append(tuple)
    for tup in removed_tuples:
        tupleArrayList.remove(tup)
    return tuples

def search_for_collar(Qrip: str) -> str:
    for tuple in tupleArrayList:
        if tuple.node1 == tuple.node2 and Qrip == tuple.node2:
            tupleArrayList.remove(tuple)
            return f"({tuple.trans})*"
    return ""

def main():
    number_of_middle_nodes = int(input())
    full_stack_with_nodes(number_of_middle_nodes)

    number_of_transitions = int(input())

    for _ in range(number_of_transitions):
        s = input()
        list_of_input_transition = s.split()
        tuple = Tuple(list_of_input_transition[0], list_of_input_transition[1], list_of_input_transition[2])
        check_for_existing_tuple(tuple)

    start_tuple = Tuple("START", "0", "0")
    tupleArrayList.append(start_tuple)

    number_of_final_states = int(input())
    final_states = input().split()
    for final_state in final_states:
        tuple = Tuple(final_state, "0", "FINAL")
        tupleArrayList.append(tuple)

    remove_state()
    result = tupleArrayList[0].trans
    result = result.replace("0", "()")
    print(result)

if __name__ == "__main__":
    main()

