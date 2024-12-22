def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    # Initialize the scoring matrix
    n, m = len(seq1), len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize gap penalties
    for i in range(n + 1):
        score_matrix[i][0] = i * gap
    for j in range(m + 1):
        score_matrix[0][j] = j * gap

    # Fill the scoring matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = score_matrix[i - 1][j - 1] + (
                match if seq1[i - 1] == seq2[j - 1] else mismatch
            )
            delete = score_matrix[i - 1][j] + gap
            insert = score_matrix[i][j - 1] + gap
            score_matrix[i][j] = max(match_score, delete, insert)

    # Traceback to reconstruct alignment
    alignment1, alignment2 = "", ""
    i, j = n, m
    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if (
            i > 0
            and j > 0
            and current_score
            == score_matrix[i - 1][j - 1]
            + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
        ):
            alignment1 = seq1[i - 1] + alignment1
            alignment2 = seq2[j - 1] + alignment2
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i - 1][j] + gap:
            alignment1 = seq1[i - 1] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = seq2[j - 1] + alignment2
            j -= 1

    return alignment1, alignment2, score_matrix[n][m]


if __name__ == "__main__":
    # Example usage
    seq1 = "CAGGTAGTG"
    seq2 = "CTAGTAG"
    alignment1, alignment2, score = needleman_wunsch(seq2, seq1)
    print("Alignment 1:", alignment1)
    print("Alignment 2:", alignment2)
    print("Score:", score)
