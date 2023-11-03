# predecessors.py
from collections import namedtuple


Address = namedtuple('Address', 'step value')

class Predecessors:
    def __init__(self, start_address):
        self.predecessors = {start_address: 0}

    def insert(self, current_address, pred_address):
        self.predecessors[current_address] = pred_address

    def __str__(self):
        result = []
        for key, value in self.predecessors.items():
            result.append(f"{key}: {value}")
        return ", ".join(result)

    def __repr__(self):
        result = []
        for key, value in self.predecessors.items():
            result.append(f"{key}: {value}")
        return ", ".join(result)

    def get_current_items(self, end_address):
        result = [end_address]
        if end_address not in self.predecessors.keys():
            raise IndexError("End address not present")

        current_address = self.predecessors[end_address]
        while current_address: # traverse to None
            if current_address != (0, 0):
                result.append(current_address)
            current_address = self.predecessors[current_address]
        result.reverse()    
        return result

    def get_current_banknotes(self, end_address):
        items = self.get_current_items(end_address)
        return map(lambda item: item.value, items)

    def get_current_path_str(self, end_address):
        result = []
        path_list = self.get_current_items(end_address)        
        for item in path_list:
            result.append((f"{item.step:3}: {item.value}"))
        return ", ".join(result)

    def get_current_path_sum(self, end_address):
        result = 0
        path_list = self.get_current_items(end_address)        
        result = sum(map(lambda item: item.value, path_list))       
        return result


if __name__ == "__main__":
    print("Create Predecessors")
    predesessor = Predecessors(Address(0, 0))

    print("Create 0 1000")
    predesessor.insert(Address(0, 1000), None)
    print("Insert 1 1000")
    predesessor.insert(Address(1, 1000), Address(0, 1000))
    print("Insert 2 500, 4 500")
    predesessor.insert(Address(2, 500), Address(1, 1000))
    predesessor.insert(Address(3, 500), Address(2, 500))
    print(f"{predesessor.predecessors=}")
    print("Insert 200")
    predesessor.insert(Address(4, 200), Address(3, 500))
    print(f"{predesessor.predecessors=}")
    print(predesessor)

    print()

    print("Insert 100 at 3")
    predesessor.insert(Address(3, 100), Address(2, 500))
    print(predesessor)

    # test get_current_path_list
    print(predesessor.get_current_items(Address(2, 500)))

    # test differents path
    print(predesessor.get_current_items(Address(4, 200)))
    print(predesessor.get_current_items(Address(3, 100)))

    # get_current_path_str
    print("get_current_path_str")
    print("(4, 200)", predesessor.get_current_path_str(Address(4, 200)))
    print("(3, 100)", predesessor.get_current_path_str(Address(3, 100)))

    # get_current_sum
    print("get_current_sum")
    print("(4, 200)", predesessor.get_current_path_sum(Address(4, 200)))
    print("(3, 100)", predesessor.get_current_path_sum(Address(3, 100)))
