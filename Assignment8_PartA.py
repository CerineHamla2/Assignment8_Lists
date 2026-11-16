
def Sudoku(list1):
    '''Checks whether a list of Sudoku numbers is valid by checking the format, values, and duplicates.'''
    if type(list1) != list:
        raise TypeError("Invalid input, please enter a valid list of numbers")

    num = [1,2,3,4,5,6,7,8,9]   ########same as i did 

    if len(list1) == 3 and all(type(row) == list for row in list1):    #checking if the list is a list of lists and has exactly 3 subgrids
        
        for row in list1:
            if len(row) != 3:
                raise ValueError("row:",row,"has more or fewer than 3 elements, each row must contain exactly 3 numbers")

            for value in row:
                if type(value) != int :
                    raise TypeError(value, "is not a number, please enter a valid number between 1 and 9")
                if  value not in num:
                    raise ValueError(i,"is Illegal value, please enter a number between 1 and 9")
                # Check duplicates within the same row
                if row.count(value) > 1:
                    raise ValueError(value, "is a duplicate value in row:", row)

        # Check duplicates between different rows
        for i in range(len(list1)):
            for j in range(i + 1, len(list1)):
                for value in list1[i]:
                    if value in list1[j]:
                        raise ValueError(value, "is a duplicate value in row:", list1[i], "and row:", list1[j])

    else:    ##the list is a single list of numbers
        for i in list1:
            if i not in num:
                raise ValueError(i,"is Illegal value, please enter a number between 1 and 9")

            else:
                if list1.count(i)>1:
                    return print(i," is a duplicate value in ", list1, ", please enter a number between 1 and 9")
    return print("valid Sudoku numbers") ###in the case where no exception is raised means all the values,format,type are valid .

            
Sudoku([1,2,3,4,5,6,7,8,9])

Sudoku([[5, 3, 4], [6, 7, 2], [1, 9, 8]])

Sudoku([[9, 9, 2], [3, 4, 8], [5, 6, 7]])

Sudoku([[8, 5, 9], [4, 2, 6], [8, 1, 3]])

Sudoku([[7, 6, 1], [6, 8, 5], [3, 9, 6]])

Sudoku([[6, 7, 8], [1, 9, 5, 3], [3, 4, 2]])
Sudoku([[4, 2, 'E'], [7, 9 , 'I'], [8, 'S', 6]])



            
           