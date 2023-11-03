# test_dfs_selection_banknotes.py
"""
Тестування алгоритма підбору банкнот за допомогою аглоритма DFS
"""
from dfs_selection_banknotes import dfs_banknotes
from cash_storage import CashStorage


def is_param_None(value, message):
    if not value:
        print(f"Error, {message}")
        return
    return True


def test_dfs_banknotes(name=None, dct_storage={}, goal=None, lst_result=None, fail=False):
    if not is_param_None(name, "Do not set name test"):
        return
    if not is_param_None(dct_storage, "Do not set dct_storage"):
        return
    if not is_param_None(goal, "Do not set goal for selection"):
        return

    print(f"Begin test {name}")
    result = dfs_banknotes(dct_storage, goal)
    # print(f"Selection {goal} from {dct_storage}, result={result}")

    if not result:
        # Select will be not success
        if fail:
            # test does not be passed
            print(f"Test {name} -== passed ==- with fallied")
            print("-" * 30)
            print()
        return
    if sum(result) != goal:
        print("Selection sum do not select")
        print("-" * 30)
        print()
        return

    print(f"Selection {goal} from {dct_storage}, result={result}")
    print(f"Test {name} -== passed ==-")
    print("-" * 30)
    print()


if __name__ == "__main__":
    # A simple test to check the performance of the algorithm
    
    test_dfs_banknotes(
        name="A simple test to check the performance of the algorithm", 
        dct_storage={"20":5, "50":4, "100":2},
        goal=110,
        )

    test_dfs_banknotes(
        name="Case 1", 
        dct_storage={5:2, 20:7, 200:3, 100:2, 1000:23},
        goal=535,
        fail=True
        )

    test_dfs_banknotes(
        name="Case 2", 
        dct_storage={5:2, 20:7, 200:3, 100:2, 1000:23},
        goal=525,
        )


    # test 110 без 10
    test_dfs_banknotes(
        name="test 110 without 10", 
        dct_storage={20:5, 50:4, 100:2},
        goal=110,
        )

    # Valerii Danilov  1170 1100 до 1200)
    test_dfs_banknotes(
        name="Valerii Danilov 1170", 
        dct_storage={1000:5, 500:1, 200:4, 100:0, 50:1, 20:1, 10:5},
        goal=1170,
        )

    test_dfs_banknotes(
        name="Valerii Danilov 1100", 
        dct_storage={1000:5, 500:1, 200:4, 100:0, 50:1, 20:1, 10:5},
        goal=1100,
        )

    test_dfs_banknotes(
        name="Valerii Danilov 1190", 
        dct_storage={1000:5, 500:1, 200:4, 100:0, 50:1, 20:1, 10:5},
        goal=1190,
        )
    
    test_dfs_banknotes(
        name="Valerii Danilov 1200", 
        dct_storage={1000:5, 500:1, 200:4, 100:0, 50:1, 20:1, 10:5},
        goal=1200,
        )

    # my find variants
    test_dfs_banknotes(
        name="my find variants 1", 
        dct_storage={10:3, 20:3, 50:0, 100:4, 200:5, 500:1, 1000:5},
        goal=3990,
        )

    test_dfs_banknotes(
        name="my find variants 2", 
        dct_storage={10:5, 20:1, 50:2, 100:0, 200:1, 500:2, 1000:4},
        goal=4300,
        )

    test_dfs_banknotes(
        name="my find variants 3", 
        dct_storage={10:5, 20:1, 50:2, 100:2, 200:0, 500:2, 1000:4},
        goal=4300,
        )

    print()
    print("Random 20 tests:")
    print("-" * 10)
    import random
    
    for idx in range(20):
        
        rand_goal = random.randint(1, 700) * 10
        dct_storage = {key:random.randint(0,5) for key in CashStorage.BANKNOTES}
        while rand_goal > CashStorage(dct_storage).available_sum():
            rand_goal = random.randint(1, 700) * 10
            dct_storage = {key:random.randint(0,5) for key in CashStorage.BANKNOTES}

        test_dfs_banknotes(
            name=f"Random test {idx+1}", 
            dct_storage=dct_storage,
            goal=rand_goal,
            )

