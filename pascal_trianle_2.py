def getRow(rowIndex):
    triangle = []
    for i in range(rowIndex + 1):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle[rowIndex]

row=int(input("Row="))
print(getRow(row))