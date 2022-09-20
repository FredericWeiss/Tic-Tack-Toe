import numpy as np
from Assignments import assignments


class Game:
    def __init__(self):
        self.separator = "---------------"
        self.row = ""
        self.example_row = ""
        self.array = np.array([["   ", " | ", "   ", " | ", "   "],
                               ["   ", " | ", "   ", " | ", "   "],
                               ["   ", " | ", "   ", " | ", "   "],
                               ],
                              dtype="object")
        self.example = np.array([[" 1 ", " | ", " 2 ", " | ", " 3 "],
                                 [" 4 ", " | ", " 5 ", " | ", " 6 "],
                                 [" 7 ", " | ", " 8 ", " | ", " 9 "],
                                 ],
                                dtype="object")

    def show_game(self):
        for n in range(0, 3):
            self.row = ""
            self.example_row = ""
            for component in self.array[n]:
                self.row = self.row + component
            for component in self.example[n]:
                self.example_row = self.example_row + component
            print(f"{self.row}         {self.example_row}")
            if n < 2:
                print(f"{self.separator}         {self.separator}")

    def validate_entry(self, entry):
        if entry < 1 or entry > 9:
            return False
        else:
            if self.array[assignments[entry][0], assignments[entry][1]] == "   ":
                return True
            else:
                return False

    def check_win(self):
        # Check for win in rows
        for n in range(0, 3):
            if self.array[n, 0] != "   ":
                if self.array[n, 0] == self.array[n, 2] and self.array[n, 0] == self.array[n, 4]:
                    return True

        # Check for win in columns
        for x in range(0, 5):
            if x % 2 == 0:
                if self.array[0, x] != "   ":
                    if self.array[0, x] == self.array[1, x] and self.array[0, x] == self.array[2, x]:
                        return True

        # Check for win in Diagonal
        if self.array[0, 0] != "   ":
            if self.array[0, 0] == self.array[1, 2] and self.array[0, 0] == self.array[2, 4]:
                return True
        if self.array[2, 0] != "   ":
            if self.array[2, 0] == self.array[1, 2] and self.array[2, 0] == self.array[0, 4]:
                return True
            else:
                return False

    def field_full(self):
        full = True
        for n in range(0, 3):
            if "   " in self.array[n]:
                full = False
        if full:
            return True
        return False
