POSSIBLE_TESTS = ['M', 'C', 'P', 'R', 'B']

class CraftingTest(object):
    def __init__(self, test):
        self.test = test ## should be a property
        self.PCs = [] ## also property
        self.mod ## readonly property that gets set when PCs are set
        return
