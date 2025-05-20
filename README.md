# Sparse Matrix Assignment – DSA HW01

 Assignment Summary

This project is part of my **Data Structures and Algorithms** course. The task was to read two sparse matrices from text files, perform operations (addition, subtraction, multiplication), and output the result in the same sparse format.

Sparse matrices are matrices where most of the values are zeros. To save memory, only non-zero values are stored and processed.

 Features

* Reads two sparse matrices from `.txt` files.
* Supports three operations:

  * Addition
  * Subtraction
  * Multiplication
* Handles input formatting errors.
* Allows saving the result to a file.

 How It Works

1. The code lists all `.txt` files in the directory.
2. The user selects two matrix files.
3. The user chooses the operation to perform.
4. The result is printed and can be saved.

 Input Format Example

```text
rows=3
cols=3
(0,1,5)
(1,2,-3)
(2,0,4)
```

Each line after `rows` and `cols` shows:
(row index, column index, value)

 Run the Code

```bash
python sparse_matrix.py
```

Make sure at least two `.txt` files are in the same folder as the script.

 Output Format

Same as input:

```text
rows=3
cols=3
(0,1,10)
(1,2,-6)
```

