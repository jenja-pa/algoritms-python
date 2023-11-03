# dfs_selection_banknotes.py
# Реалізація алгоритма підбору купюр до потрібної суми із переліку наявних

from stack import Stack
from cash_storage import CashStorage
from predecessors import Predecessors, Address


def is_legal_increase_step(banknote, current_sum, goal):
    """
    Перевірка чи не перевищує сума прирощення (banknote) потрібну суму підбору (goal)
    поточна наявна сума - (current_sum)
    """
    return current_sum + banknote <= goal


def dfs_banknotes(dict_storage, goal):
    """
    Алгоритм підбору суми goal(числове значення) із банкнот наявних у сховищі банкнот
    яке задається словником відповідного формату
    за допомогою метода пошуку в глибину (DFS)
    """
    storage = CashStorage(init_cash_storage=dict_storage)
    atm_present_sum = storage.available_sum()
    if atm_present_sum < goal:
        print(f"Error - insufficient funds: storage contain: {atm_present_sum}, need sum: {goal}")
        return None
    
    step = 0
    stack = Stack()
    start_address = Address(step, 0)
    predecessors = Predecessors(start_address)
    # insertion all legale variants increase
    for banknote in storage.available_banknotes:
        if is_legal_increase_step(banknote, 0, goal):
            stack.push(Address(step, banknote))
            predecessors.insert(Address(step, banknote), start_address)
    # print("test print init DFS")
    # print(f"{stack=}")
    # print(f"{predecessors=}")

    while not stack.is_empty():
        # 1 extract next item from stack
        current_address = stack.pop()

        current_sum = predecessors.get_current_path_sum(current_address)
        # print(f"({step}) {current_address=}, {current_sum=} {stack=}")
        if current_sum == goal:
            print(f"Goal achived in {step} steps")
            lst_selected_banknotes = list(
                predecessors.get_current_banknotes(current_address)
                )
            # print(f"Selected banknotes: {lst_selected_banknotes}")
            return lst_selected_banknotes
        elif predecessors.get_current_path_sum(current_address) > goal:
            # Sum larger that need, back to get smaller sum 
            continue
        else:
            # print("Else ")
            step += 1
            # print(f"step:{step}")
            modify_self_storage = CashStorage(storage.get_dict_storage)
            selected_banknotes = list(predecessors.get_current_banknotes(current_address))
            modify_self_storage.sub_banknotes(selected_banknotes)
            # print(f"{modify_self.atm_storage}")
            
            for banknote in modify_self_storage.available_banknotes_LE_them(current_address.value):
                if is_legal_increase_step(banknote, current_sum, goal):
                    stack.push(Address(step, banknote))
                    predecessors.insert(Address(step, banknote), current_address)
        if step > 20000:
            print("Too many steps, break search")
            break

    print(f"Warning: DFS algoritm spent: {step} steps, but target {goal} not achived for this storage: ")
    print(f"{storage.show()}")
    print("-" * 25)
    print()
    return None

if __name__ == "__main__":
    # # A simple test to check the performance of the algorithm
    # goal = 110
    # inp_dict = {"20":5, "50":4, "100":2}
    # result = dfs_banknotes(inp_dict, goal)
    # print(f"Selection {goal} from {inp_dict}, result={result}")

    # Wromg work algoritm
    goal = 4280
    inp_dict = {5:0, 10:0, 20:5, 50:0, 100:0, 500:5, 1000:4}
    result = dfs_banknotes(inp_dict, goal)
    print(f"Selection {goal} from {inp_dict}, result={result}")
