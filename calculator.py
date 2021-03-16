def type_of_var(variable):
    if '.' in variable:
        return float(variable)
    else:
        return int(variable)


def result(matrix_):
    print('The result is:')
    for i in matrix_:
        string = ''
        for j in i:
            string = string + str(j) + ' '
        print(string.rstrip())

if __name__ == "__main__":
    choose = '5'
    while choose != '0':
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('0. Exit')
        choose = input('Your choice: > ')

        if choose == '1':
            rows1, columns1 = map(int, input('Enter size of first matrix: > ').split())
            print('Enter first matrix:')
            matrix1 = [input('> ').split() for i in range(rows1)]
            rows2, columns2 = map(int, input('Enter size of second matrix: > ').split())
            if not (columns1 == columns2 and rows1 == rows2):
                print('ERROR')
            else:
                print('Enter second matrix:')
                matrix2 = [input('> ').split() for i in range(rows2)]
                for i in range(rows1):
                    for j in range(columns1):
                        matrix1[i][j] = type_of_var(matrix1[i][j]) + type_of_var(matrix2[i][j])
                result(matrix1)
            print('\n')

        if choose == '2':
            rows1, columns1 = map(int, input('Enter size of matrix: > ').split())
            print('Enter matrix:')
            matrix1 = [input('> ').split() for i in range(rows1)]
            constant = type_of_var(input('Enter constant: > '))
            for i in range(rows1):
                for j in range(columns1):
                    matrix1[i][j] = type_of_var(matrix1[i][j]) * constant
            result(matrix1)
        print('\n')

        if choose == '3':
            rows1, columns1 = map(int, input('Enter size of first matrix: > ').split())
            print('Enter first matrix:')
            matrix1 = [input('> ').split() for i in range(rows1)]
            rows2, columns2 = map(int, input('Enter size of second matrix: > ').split())
            if not (columns1 == rows2):
                print('ERROR')
            else:
                product = [[0 for j in range(columns2)] for i in range(rows1)]
                print('Enter second matrix: > ')
                matrix2 = [input('> ').split() for i in range(rows2)]

                for i in range(len(matrix1)):
                    for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                            product[i][j] += type_of_var(matrix1[i][k]) * type_of_var(matrix2[k][j])
                result(product)

        if choose == '4':
            print('1. Main diagonal')
            print('2. Side diagonal')
            print('3. Vertical line')
            print('4. Horizontal line')
            choose_t = input('Your choice: > ')
            rows, columns = map(int, input('Enter matrix size: > ').split())
            print('Enter matrix:')
            matrix = [input('> ').split() for i in range(rows)]
            if choose_t == '1':  # transposition along the main diagonal
                transpose = [[type_of_var(row[i]) for row in matrix] for i in range(len(matrix[0]))]
                result(transpose)
            if choose_t == '2':  # transposition along the side diagonal
                transpose = [[row[(-(i + 1))] for row in matrix[::-1]] for i in range(len(matrix[0]))]
                result(transpose)
            if choose_t == '3':  # transposition along the vertical line
                transpose = [[j for j in i[::-1]] for i in matrix]
                result(transpose)
            if choose_t == '4':  # transposition along the horizontal line
                transpose = [i for i in matrix[::-1]]
                result(transpose)