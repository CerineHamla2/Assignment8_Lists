# Assignment8_Lists
#  Sudoku and NLP

## 1. Program Descriptions

**Sudoku Function:**

The `Sudoku()` function checks whether a list of numbers is valid for a Sudoku 3×3 grid. It accepts either a single list or a list of three sublists. The function checks that the numbers are between 1 and 9, that there are no duplicates, and that the input follows the correct format. If something is wrong, it raises an error or prints a message explaining the issue. Otherwise, it prints `"valid Sudoku numbers"`.

**NLP Function:**

The `NLP()` function takes a string of text and counts the number of unique words, without counting repeated words more than once. It also has an optional argument called `common`, which allows the user to display a certain number of the most frequently occurring words and how many times they appear.

## 2. How to Run the Programs

Run the Python file in VS Code. Both functions can be tested by calling them with different inputs.

**Sudoku Examples:**

```python
Sudoku([1,2,3,4,5,6,7,8,9])
Sudoku([[5,3,4],[6,7,2],[1,9,8]])
Sudoku([[9,9,2],[3,4,8],[5,6,7]])
```

The first two examples are valid, while the third contains a duplicate number and raises an error.

**NLP Examples:**

```python
NLP("The sun is bright and the stars are bright", 2)
NLP("The sun is bright and the stars are bright", 2)
```

Expected outcome: 
First example : there is: 7 unique word
2nd example:
Most common word: "the" appeared: 2 times
Most common word: "bright" appeared: 2 times
there is: 7 unique word


For testing, I also used all six stanzas of Edgar Allan Poe's *Annabel Lee* separately, followed by the entire poem.

## 3. Sources and Contributors

- **Source:** lecture slides. Python built-in functions and methods.
