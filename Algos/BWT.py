class BurrowsWheel:
    def __init__(self, sequence):
        self.sequence = sequence
        self.bwt = ""

    def __occ(self, symbol):
        i = 0
        for char in self.bwt:
            if char < symbol:
                i += 1
        return i

    def __counts(self, position, symbol):
        i = 0
        for j in range(position):
            if self.bwt[j] == symbol:
                i += 1
        return i

    def left_walk(self, position, symbol):
        return self.__occ(symbol) + self.__counts(position, symbol)

    def burrows_wheelers_transform(self):
        bwm, rotations, rotation = [], [], []

        for i in range(len(self.sequence)):
            rotation = self.sequence[i:] + self.sequence[:i]
            rotations.append(rotation)

        rotations = sorted(rotations)
        bwm = [rotation for rotation in rotations]
        for i in bwm:
            self.bwt += i[-1]
        return self.bwt


if __name__ == "__main__":
    # Example usage:
    input_string = "acaacg$"
    obj = BurrowsWheel(input_string)

    # Print BWT
    print("------------------------BWT:----------------------")
    bwt = obj.burrows_wheelers_transform()
    print(bwt)

    # Get mapping
    i = obj.left_walk(6, "c")
    print("Mapping: ", i)

    i = obj.left_walk(4, "a")
    print("Mapping: ", i)

    i = obj.left_walk(0, "g")
    print("Mapping: ", i)

    i = 0
    t = ""
    while bwt[i] != "$":
        t = bwt[i] + t
        i = obj.left_walk(i, bwt[i])
    print("Original String: ", t)

    query_seq = "aac"
    top = 0
    bottom = len(input_string)
    for query_char in query_seq[::-1]:
        top = obj.left_walk(top, query_char)
        bottom = obj.left_walk(bottom, query_char)

    print("Top: ", top)
    print("Bottom: ", bottom)

    print()
