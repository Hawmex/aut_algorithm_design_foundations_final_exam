# Algorithm Design Foundations
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

    # Create a matrix to store the lengths of common subsequences
    lengths = [[0] * (string2_length + 1) for _ in range(string1_length + 1)]

    # Initialize the maximum length of the common subsequence
    max_length = 0

    # Initialize the start index of the common subsequence in string1
    start1_index = 0

    # Initialize the start index of the common subsequence in string2
    start2_index = 0

    for i in range(1, string1_length + 1):
        for j in range(1, string2_length + 1):
            # If the characters at the corresponding positions are equal
            if string1[i - 1] == string2[j - 1]:
                # Update the length of the common subsequence
                lengths[i][j] = lengths[i - 1][j - 1] + 1

                # If the current length is greater than the maximum length
                if lengths[i][j] > max_length:
                    max_length = lengths[i][j]  # Update the maximum length

                    start1_index = i - max_length  # Update the start index in string1
                    start2_index = j - max_length  # Update the start index in string2

    print(f"{start1_index} {start2_index} {max_length}")


def main():
    # Accept two strings separated by a space as input and pass them to the
    # `print_lcs_details` function
    print_lcs_details(*input().split(" "))


if __name__ == "__main__":
    main()
