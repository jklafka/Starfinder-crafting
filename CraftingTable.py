import numpy as np
from CraftingTask import CraftingTask

POSSIBLE_TESTS = ['M', 'C', 'P', 'R', 'B']

class CraftingTable(object):

    def __init__(self, ref):
        self.__prev_jumps = []
        self.__seed = np.random.random() #however you want set this
        self.__craftingSheets = self.__getCraftingSheets(ref)
        self.__tests ## turn this into a property
        return

    def generate_tests(self) -> List:
        item = input("Choose an item")
        self.__tests = []
        self.__tests.append((self.__first_test(), 0))
        for _ in range(5): #whatever the logic is
            test = self.__choose_test()
            jump = self.jump()
            if test == self.__tests[-1]:
                continue
            self.__tests.append(test)
        return []

    def __first_test(self) -> CraftingTest:
        # First test is just max of fabrication weights
        test = max(self.__craftingSheets["fab_weights"])
        return test

    def __choose_test(self) -> CraftingTest:
        # Pseudo-random number generator
        # e.g. linear congruential generator
        t = CraftingTest('B') # 'B' is last
        a = random.randint() * 2000
        for testName in POSSIBLE_TESTS:
            a -= this.__craftingSheets["fab_weights"][testname]
            if a < 0:
                t = CraftingTest(testName)
        return t

    def __jump(self) -> int:
        p = np.random.normal(0, 1)
        if (p < -1) and (self.__prev_jumps != [0,0,0]):
            next_jump = 0
        elif p > 1:
            next_jump = 2
        else:
            next_jump = 1
        if len(self.__prev_jumps > 0):
            self.__prev_jumps.pop()
        self.__prev_jumps.append(next_jump)
        return next_jump

    def __getCraftingSheets(self, googlesheetRef) -> None:
        # get the crafting table from Chuck's google sheet
        return {}
