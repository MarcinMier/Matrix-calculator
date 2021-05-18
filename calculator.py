def type_of_var(variable):
    if '.' in variable:
        return float(variable)
    else:
        return int(variable)


def result(matrixr):
    print('The result is:')
    for i in matrixr:
        r_string = ''
        for j in i:
            r_string = r_string + str(j) + ' '
        print(r_string.rstrip())


def det(tab_d):
    if len(tab_d) == 1:
        return tab_d[0][0]
    elif len(tab_d) == 2:
        return tab_d[0][0] * tab_d[1][1] - tab_d[1][0] * tab_d[0][1]
    else:
        tab_minors = []
        for pos, element in enumerate(tab_d[0]):
            tab_minor = []
            for column in tab_d[1:]:
                row_smaller = []
                row_smaller.extend(column[:pos])
                row_smaller.extend(column[(pos + 1):])
                tab_minor.append(row_smaller)
            tab_minors.append(tab_minor)
        det_sum = 0
        for t, t_ms, factor in zip(tab_d[0], tab_minors, range(len(tab_d))):
            det_sum += t * det(t_ms) * (-1) ** (factor % 2)
        return det_sum



if __name__ == "__main__":
    choose = '6'
    while choose != '0':
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('6. Inverse matrix')
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

        if choose == '5':
            rows, columns = map(int, input('Enter matrix size: > ').split())
            if rows != columns:
                print('ERROR')
                continue
            print('Enter matrix:')
            matrix = [input('> ').split() for i in range(rows)]
            matrix = [[type_of_var(j) for j in i] for i in matrix]
            print('The result is:')
            print(det(matrix), '\n')

        if choose == '6':
            rows, columns = map(int, input('Enter matrix size: > ').split())
            if rows != columns:
                print('ERROR')
                continue
            print('Enter matrix:')
            matrix = [input('> ').split() for i in range(rows)]
            matrix = [[type_of_var(j) for j in i] for i in matrix]
            d = det(matrix)
            if d == 0:
                print("This matrix doesn't have an inverse.")
                continue
            else:
                inverse_det = 1 / det(matrix)
                row_to_det = 0
                tab_to_det = []
                for by_row in matrix:
                    column_to_det = 0
                    row_of_tab_to_det = []
                    for by_column in by_row:
                        new_tab = []
                        for row_number, row in enumerate(matrix):
                            new_row = []
                            for column_number, column in enumerate(row):
                                if column_number != column_to_det and row_number != row_to_det:
                                    new_row.append(column)
                            if new_row:
                                new_tab.append(new_row)
                        column_to_det += 1
                        row_of_tab_to_det.append(det(new_tab))
                    tab_to_det.append(row_of_tab_to_det)
                    row_to_det += 1
                tab_proper_sign = []
                for row_to_power_number, row_to_power in enumerate(tab_to_det):
                    row_proper_sign = []
                    for col_to_pow_num, col_to_pow in enumerate(row_to_power):
                        row_proper_sign.append(col_to_pow * ((-1) ** (col_to_pow_num + 1 + row_to_power_number + 1)))
                    tab_proper_sign.append(row_proper_sign)
                transposed = [[row[i] for row in tab_proper_sign] for i in range(len(tab_proper_sign[0]))]
                for m in range(len(transposed)):
                    for n in range(len(transposed[0])):
                        transposed[m][n] = float(transposed[m][n] * inverse_det)
                        if transposed[m][n] in (-0.0, 0.0):
                            transposed[m][n] = 0
                print('The result is:')
                for row_result in transposed:
                    result_string_row = ''
                    for column_result in row_result:
                        result_string_char = str(column_result)
                        dot_present = 0
                        for char_pos, char in enumerate(str(column_result)):
                            if char == '.':
                                dot_present = char_pos
                                break
                        if dot_present != 0:
                            result_string_char = result_string_char[:(dot_present + 3)]
                        result_string_row = result_string_row + result_string_char + ' '
                    print(result_string_row)
                print('\n')
