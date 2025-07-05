def burrows_wheelers_transform(s):
    BWT: str = ""
    bwm, rotations, rotation = [], [], []

    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        rotations.append(rotation)

    rotations = sorted(rotations)

    bwm = [rotation for rotation in rotations]
    for i in bwm:
        BWT += i[-1]

    return BWT, bwm


if __name__ == "__main__":
    # Example usage:
    input_string = "acaacg$"
    bwt, bwm = burrows_wheelers_transform(input_string)

    # Print all rotations
    print("------------------------Rotations:---------------------")
    for i in bwm:
        print(i)

    # Print BWT
    print("------------------------BWT:----------------------\n", bwt)
