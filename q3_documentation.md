# Principles of Algorithm Design

## Final Exam, Question 3

## Student Name

Hamed Araab

## Student Number

9925003

## Introduction

This documentation provides an overview of the code implementation for finding the Longest Common Subsequence (LCS) between two strings. The code uses the principles of Algorithm Design and employs the Dynamic Programming approach to efficiently compute the LCS.

## Code Structure

The code consists of the following components:

1. `print_lcs_details` function: Finds the LCS between two strings and prints the start index of LCS in each string and the length of LCS.
2. `main` function: Provides the user interface for input and output handling.

## `print_lcs_details` Function

### Function Description

The `print_lcs_details` function calculates the LCS between two strings and prints the start index of LCS in each string and the length of LCS.

### Function Parameters

- `string1`: The first input string.
- `string2`: The second input string.

### Function Steps

1. Initialize variables `string1_length` and `string2_length` with the lengths of `string1` and `string2`, respectively.
2. Create a 2D array `lengths` with dimensions `(string1_length + 1) x (string2_length + 1)`. Initialize all elements to 0.
3. Initialize variables `max_length`, `start1_index`, and `start2_index` to track the maximum length of LCS and the corresponding start indices.
4. Iterate over the indices `i` from 1 to `string1_length` and `j` from 1 to `string2_length`.
5. If the characters at indices `i-1` in `string1` and `j-1` in `string2` are equal, update `lengths[i][j]` by adding 1 to `lengths[i-1][j-1]`.
6. If `lengths[i][j]` is greater than `max_length`, update `max_length` and set `start1_index` to `i - max_length` and `start2_index` to `j - max_length`.
7. Print the values of `start1_index`, `start2_index`, and `max_length` in the format `start1_index start2_index max_length`.

### `main` Function

#### Function Description

The `main` function is the entry point of the program. It handles user input and output.

#### Function Steps

1. Reads two strings separated by a space from the user.
2. Calls the `print_lcs_details` function with the two input strings.

## Usage Example

```python
print_lcs_details(*input().split(" "))
```

The user is prompted to provide two strings separated by a space. The code then calculates the LCS between the two strings and prints the start index of LCS in each string and the length of LCS.

## Conclusion

This documentation provided an overview of the code implementation for finding the Longest Common Subsequence (LCS) between two strings. The code follows the principles of Algorithm Design and employs the Dynamic Programming approach to efficiently compute the LCS. The provided `print_lcs_details` function accepts two strings, calculates the LCS, and prints the start indices and length of LCS.
