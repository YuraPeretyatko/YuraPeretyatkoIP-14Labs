import math

def sort_columns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for col in range(cols):
        for i in range(rows):
            for j in range(0, rows - i - 1):
                if matrix[j][col] > matrix[j + 1][col]:
                    matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]
    return matrix

def geometric(row):
    product = 1
    for x in row:
        product *= abs(x)  
    return product**(1/len(row))

def main():
    matrix = [
        [66, 21, -3, -1, 90],
        [1, 74, -2, 80, -1],
        [10, 30, 20, -50, 91],
        [2, 4, 5, 81, 0],
        [33, 69, -5, 51, 24]
    ]

    sorted_matrix = sort_columns(matrix)

    fi_values = [geometric(row) for row in sorted_matrix]

    F_value = sum(fi_values) / len(fi_values)

    print("Відсортована матриця:")
    for row in sorted_matrix:
        print(row)

    print("\n значення fi(aij):")
    for i, fi in enumerate(fi_values, start=1):
        print(f"Рядок {i}: {fi:.4f}")

    print(f"\n значення F(fi(aij)): {F_value:.4f}")

if __name__ == "__main__":
    main()
