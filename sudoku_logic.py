""" This is the logic component for the sudoku solver """

import math

def calculate(values):
    if validate(values) != True:
        """ Exit! """
        return

    gridArray = formatValues(values)

    calculationPass(gridArray)

def calculationPass(gridArray):
    """ Go through the rows and columns """

    rows = getRows(gridArray)
    columns = getColumns(gridArray)

    for i in range (1, 10):
        # Go throgh each number in turn
        print "checking for %d" % i

        possibilityGrid = getPossibilityGrid()

        for rowNumber, row in enumerate(rows):
            if i in row:
                # First mark the row
                gridRow = int(math.floor(rowNumber / 3))
                subGridRow = rowNumber if rowNumber < 3 else (rowNumber % 3)

                print gridRow
                print subGridRow

                for j, possibilityGridBox in enumerate(possibilityGrid):
                    if j in [3 * gridRow, 3 * gridRow + 1, 3 * gridRow + 2]:
                        possibilityGridBox[3 * subGridRow] = 0
                        possibilityGridBox[3 * subGridRow + 1] = 0
                        possibilityGridBox[3 * subGridRow + 2] = 0


        # Then mark the grid

        print possibilityGrid

def getRows(gridArray):
    rows = []

    for i in range(0, 3):
        for j in range(0, 3):
            row = []
            row.append(gridArray[3 * i][3 * j])
            row.append(gridArray[3 * i][3 * j + 1])
            row.append(gridArray[3 * i][3 * j + 2])
            row.append(gridArray[3 * i + 1][3 * j])
            row.append(gridArray[3 * i + 1][3 * j + 1])
            row.append(gridArray[3 * i + 1][3 * j + 2])
            row.append(gridArray[3 * i + 2][3 * j])
            row.append(gridArray[3 * i + 2][3 * j + 1])
            row.append(gridArray[3 * i + 2][3 * j + 2])

            rows.append(row)

    return rows

def getColumns(gridArray):
    columns = []

    for i in range(0, 2):
        for j in range(0, 2):
            column = []
            column.append(gridArray[i][j])
            column.append(gridArray[i][j + 3])
            column.append(gridArray[i][j + 6])
            column.append(gridArray[i + 3][j])
            column.append(gridArray[i + 3][j + 3])
            column.append(gridArray[i + 3][j + 6])
            column.append(gridArray[i + 6][j])
            column.append(gridArray[i + 6][j + 3])
            column.append(gridArray[i + 6][j + 6])

            columns.append(column)

    return columns

def getPossibilityGrid():
    return [
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1]
    ]

def validate(values):
    validated = True

    for box in values:
        for valueObj in box:
            continue
            #print valueObj
        #print "\n"

    print "validation success"

    return validated

def formatValues(values):
    """format values into an array of integers"""

    gridValues = []

    for box in values:
        subValues = []
        for valueObj in box:
            subValue = str(valueObj)

            subValues.append(int(subValue) if subValue != '' else 0)

        gridValues.append(subValues)

    return gridValues
