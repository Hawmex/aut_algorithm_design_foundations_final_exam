# Principles of Algorithm Design
#
# Final Exam, Question 3
#
# Student Name: Hamed Araab
# Student Number: 9925003


def print_lcs_details(string1, string2):
    """
    Prints:

    - The start index of LCS in `string1`.
    - The start index of LCS in `string2`.
    - The length of LCS.

    ### Example:

    Input: `"cool", "toolbox"`

    Output: `1 1 3`

    ### Notes:

    - This function uses the Dynamic Programming algorithm with `O(n * m)` time
    complexity (`m = len(string1)` and `n = len(string2)`).
    """

    string1_length = len(string1)
    string2_length = len(string2)

    lengths = [[0] * (string2_length + 1) for _ in range(string1_length + 1)]

    max_length = 0

    start1_index = 0
    start2_index = 0

    for i in range(1, string1_length + 1):
        for j in range(1, string2_length + 1):
            if string1[i - 1] == string2[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1

                if lengths[i][j] > max_length:
                    max_length = lengths[i][j]

                    start1_index = i - max_length
                    start2_index = j - max_length

    print(f"{start1_index} {start2_index} {max_length}")


def main():
    print_lcs_details(*input().split(" "))


if __name__ == "__main__":
    main()
