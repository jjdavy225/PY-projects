# Python program to find Determinant of a matrix


def determinantOfMatrix(mat, n):

    temp = [0]*n  # temporary array for storing row
    total = 1
    det = 1  # initialize result

    # loop for traversing the diagonal elements
    for i in range(0, n):
        index = i  # initialize the index

        # finding the index which has non zero value
        while (index < n and mat[index][i] == 0):
            index += 1

        if (index == n):  # if there is non zero element
            # the determinant of matrix as zero
            continue

        if (index != i):
            # loop for swapping the diagonal element row and index row
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

            # determinant sign changes when we shift rows
            # go through determinant properties
            det = det*int(pow(-1, index-i))

        # storing the values of diagonal row elements
        for j in range(0, n):
            temp[j] = mat[i][j]

        # traversing every row below the diagonal element
        for j in range(i+1, n):
            num1 = temp[i]	 # value of diagonal element
            num2 = mat[j][i]  # value of next row element

            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                # multiplying to make the diagonal
                # element and next row element equal

                mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])

            total = total * num1  # Det(kA)=kDet(A);

    # multiplying the diagonal elements to get determinant
    for i in range(0, n):
        det = det*mat[i][i]

    return int(det/total)  # Det(kA)/k=Det(A);


# Drivers code
if __name__ == "__main__":
    # mat=[[6 1 1][4 -2 5][2 8 7]]

    mat = [[1, 0, 2, -1, 50], [3, 0, 0, 5, 40],
           [2, 1, 4, -3, 5], [1, 0, 5, 0, 7], [5, 2, 4, 8, 6]]
    N = len(mat)

    # Function call
    print("Determinant of the matrix is : ", determinantOfMatrix(mat, N))
