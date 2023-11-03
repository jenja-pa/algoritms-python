# cash_storage.py
from collections.abc import Iterable

class NonAvaliableBanknoteError(ValueError):
    pass

class InvalidBanknoteForSubstractError(ValueError):
    pass

class NeedIterableError(TypeError):
    pass


class CashStorage:
    
    BANKNOTES = [5, 10, 20, 50, 100, 200, 500, 1000]
    cnt = 0
    
    def __init__(self, init_cash_storage=None, name=None):
        # process init parameters
        self.dict_storage = {}
        if init_cash_storage:
            self.set_cash_storage(init_cash_storage)

        CashStorage.cnt += 1

        self.name = f"Storage_{CashStorage.cnt}"
        if name and isinstance(name, str):
            self.name = name

    def set_cash_storage(self, value):
        if not isinstance(value, dict):
            raise TypeError("Value for cash_storage must be a dict type {<str or int>: <int - count banknote>, }")
        # init start storage
        for key in self.BANKNOTES:
            self.dict_storage[key] = 0
        # look through input data
        for key_param in value:
            try:
                internal_key = int(key_param)
            except:
                continue
            if internal_key in self.BANKNOTES:
                self.dict_storage[internal_key] = value[key_param]

    def show_detail(self):
        result = []
        result.append(f" --==  {self.name}  ==-- ")
        result.append(f"|Sum avail:{self.available_sum():11}|")
        result.append("-" * 23)
        for key, value in self.dict_storage.items():
            result.append(f"{key:5}:{value}")
        result.append("-" * 23)
        return "\n".join(result)

    def show(self):
        result = []
        shead = (f"-{self.name}- | Present: {self.available_sum()}")
        for key, value in self.dict_storage.items():
            result.append(f"{key:4}:{value}")
        return f"{shead}\n {', '.join(result)}"

    def __str__(self):
        return self.show_detail()

    def __repr__(self):
        return self.show()

    def available_sum(self):
        result = []
        for key, cnt in self.dict_storage.items():
            result.append(int(key) * cnt)
        return sum(result)

    def add_banknote(self, nominal, cnt=1):
        if nominal not in self.BANKNOTES:
            raise NonAvalErroriableBanknote
        self.dict_storage[nominal] += cnt

    def sub_banknote(self, nominal, cnt=1):
        if nominal not in self.BANKNOTES:
            raise NonAvaliableBanknoteError
        if (self.dict_storage[nominal] - cnt) < 0:
            raise InvalidBanknoteForSubstractError
        self.dict_storage[nominal] -= cnt

    def sub_banknotes(self, iter):
        if not isinstance(iter, Iterable):
            raise NeedIteratorError
        for banknote in iter:
            # print(f"test [sub_banknotes]: {banknote}")
            if banknote != 0:
                self.sub_banknote(banknote)
    def available_banknotes_LE_them(self, value):
        """
        Get list available banknotes thay less or equal value
        """
        result = []
        for key in self.dict_storage:
            if self.dict_storage[key] > 0 and key <= value:
                result.append(key)
        # result.sort(reverse=True)
        return result

    @property
    def get_dict_storage(self):
        return self.dict_storage

    @property
    def available_banknotes(self):
        """
        Get list available banknotes for current state cash storage
        """
        result = []
        for key in self.dict_storage:
            if self.dict_storage[key] > 0:
                result.append(key)
        # result.sort(reverse=True)
        return result


if __name__ == "__main__":
    # test create storage
    inp_dict = {5:3, 20:7, 200:3, 100:2, 1000: 23}
    storage = CashStorage(inp_dict, name="ATM storage")
    print(f"input dict: {inp_dict}")
    print(f"{storage.show()}")

    inp_dict = {"5":3, 17: 34, "20":7, "200": 3, "100": 2, "1000": 23}
    storage = CashStorage(inp_dict, name="ATM storage string")
    print(f"input dict: {inp_dict}")
    print(f"{storage.show()}")

    inp_dict = {5.3:3, 17.0:34, 20.45:7, 200.0: 3, 100.0: 2, 1000.34: 23}
    storage = CashStorage(inp_dict, name="ATM storage float")
    print(f"input dict: {inp_dict}")
    print(f"{storage.show()}")

    inp_dict = {5.3:3, "17.0":34, (20, 45):7, 200:3, "100_00": 2, True: 23}
    storage = CashStorage(inp_dict, name="ATM storage mixed")
    print(f"input dict: {inp_dict}")
    print(f"{storage.show()}")

    print()
    print("-" * 25)

    inp_dict = {5:3, 20:7, 200:3, 100:2, 1000: 23}
    storage = CashStorage(inp_dict, name="ATM storage")
    print(f"init storage: {storage.show()}")
    # Check operations
    print("Add 5 for 20")
    storage.add_banknote(20, 5)
    print(f"{storage.show()}")

    print("Substract correct banknotes. 5 for 1000")
    storage.sub_banknote(1000, 5)
    print(f"{storage.show()}")

    print("Substract incorrect banknotes. 5 for 200")
    try:
        storage.sub_banknote(200, 5)
    except InvalidBanknoteForSubstractError:
        print("Except. Error substract banknotes. Change not present.")
    print(f"{storage.show()}")

    print("Create new ATM storage from storage")
    storage2 = CashStorage(storage.get_dict_storage)
    print("New 2 storage from main")
    print(storage2)
    print("Modify New storage")
    storage2.sub_banknote(1000, 4)
    print(storage2)
    print(storage)
    print("-" * 25)
    print(storage2)
    banknotes = [5, 20, 20, 100, 1000, 1000]
    print(f"Sub banknotes: {banknotes}")
    storage2.sub_banknotes(banknotes)
    print(storage2)

    print("available_banknotes storage2:")
    print(storage2.available_banknotes)

    print("available_banknotes_LE_them 100")
    print(storage2.available_banknotes_LE_them(100))
