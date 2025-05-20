import os

class SparseMatrix:
    def __init__(self, rows=0, cols=0, data=None):
        self.rows = rows
        self.cols = cols
        self.data = data if data else {}

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                rows = int(lines[0].split('=')[1])
                cols = int(lines[1].split('=')[1])
                data = {}
                for line in lines[2:]:
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file has wrong format")
                    try:
                        row, col, val = line.strip('()').split(',')
                        data[(int(row), int(col))] = int(val)
                    except:
                        raise ValueError("Input file has wrong format")
                return cls(rows, cols, data)
        except Exception as e:
            raise ValueError(f"Error reading '{filename}': {e}")

    def get(self, row, col):
        return self.data.get((row, col), 0)

    def set(self, row, col, value):
        self.data[(row, col)] = value

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix sizes do not match for addition.")
        result = self.data.copy()
        for key, val in other.data.items():
            result[key] = result.get(key, 0) + val
        return SparseMatrix(self.rows, self.cols, result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix sizes do not match for subtraction.")
        result = self.data.copy()
        for key, val in other.data.items():
            result[key] = result.get(key, 0) - val
        return SparseMatrix(self.rows, self.cols, result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not allow multiplication.")
        result = {}
        B_by_row = {}
        for (k, j), valB in other.data.items():
            if k not in B_by_row:
                B_by_row[k] = []
            B_by_row[k].append((j, valB))

        for (i, k), valA in self.data.items():
            if k in B_by_row:
                for j, valB in B_by_row[k]:
                    result[(i, j)] = result.get((i, j), 0) + valA * valB

        return SparseMatrix(self.rows, other.cols, result)

    def display(self):
        for (r, c), v in sorted(self.data.items()):
            print(f"({r},{c},{v})")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (r, c), v in sorted(self.data.items()):
                file.write(f"({r},{c},{v})\n")
        print(f"Result saved to {filename}")

def list_matrix_files():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    print("Available sample input files:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    return files

# Main Program
try:
    files = list_matrix_files()
    if len(files) < 2:
        raise FileNotFoundError("Need at least two matrix files.")

    idx1 = int(input("\nSelect the first matrix by number (e.g., 1): ")) - 1
    idx2 = int(input("Select the second matrix by number (e.g., 2): ")) - 1
    m1 = SparseMatrix.from_file(files[idx1])
    m2 = SparseMatrix.from_file(files[idx2])

    print("\nChoose operation:\n1 - Addition\n2 - Subtraction\n3 - Multiplication")
    op = input("Enter choice (1/2/3): ").strip()

    if op == '1':
        result = m1.add(m2)
        print("\nResult of M1 + M2:")
        result.display()
    elif op == '2':
        result = m1.subtract(m2)
        print("\nResult of M1 - M2:")
        result.display()
    elif op == '3':
        result = m1.multiply(m2)
        print("\nResult of M1 x M2:")
        result.display()
    else:
        raise ValueError("Invalid operation choice.")

    save = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()
    if save == 'yes':
        output_file = input("Enter the name of the output file (e.g., result.txt): ").strip()
        result.save_to_file(output_file)

except Exception as e:
    print(f"\n{e}")

