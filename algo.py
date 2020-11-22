import numpy as np
from CraftingTable import CraftingTable
# import googlesheets api
# https://developers.google.com/sheets/api/

def main() -> None:
    ref = ""
    table = CraftingTable(ref)
    for test in table.tests:
        test.assignPCs()
    mod = sum([test.mod for test in table.tests])
    diceroll = np.random.randint(1, 20) + mod #whatever this is
    return diceroll

if __name__ == "__main__":
    main()
