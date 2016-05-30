""" This is the logic component for the sudoku solver """

import math

def calculate(values):
    if validate(values) != True:
        """ Exit! """
        return

    gridArray = formatValues(values)

    calculationCount = 0

    calculatedArray = calculationPass(gridArray, calculationCount)

    print calculatedArray

def calculationPass(gridArray, count):
    """ Go through the rows and columns """

    rows = getRows(gridArray)
    columns = getColumns(gridArray)

    for i in range (1, 10):
        possibilityGrid = getPossibilityGrid(gridArray)

        # Go through the rows.
        for rowNumber, row in enumerate(rows):
            if i in row:
                # 0-2 the row the grid the [i] is in.
                gridRow = int(math.floor(rowNumber / 3))
                # 0-2 the row of [i] within the grid.
                subGridRow = rowNumber if rowNumber < 3 else (rowNumber % 3)

                for j, possibilityGridBox in enumerate(possibilityGrid):
                    # Is the possiblity grid box within the row of grids that [i] appears in?
                    if j in [3 * gridRow, 3 * gridRow + 1, 3 * gridRow + 2]:
                        # Mark the full row as invalid locations.
                        possibilityGridBox[3 * subGridRow] = 0
                        possibilityGridBox[3 * subGridRow + 1] = 0
                        possibilityGridBox[3 * subGridRow + 2] = 0

                    # Mark the grids that [i] appears in.
                    if j == int(3 * gridRow + math.floor(row.index(i) / 3)):
                        for k in range(0, 9):
                            possibilityGridBox[k] = 0

        # Go through columns.
        for colNumber, col in enumerate(columns):
            if i in col:
                # 0-2 The column of the grid that [i] is in
                gridCol = int(math.floor(colNumber / 3))
                # 0-2 The column of [i] within the grid
                subGridCol = colNumber if colNumber < 3 else (colNumber % 3)

                for l, possibilityGridBox in enumerate(possibilityGrid):
                    if l in [gridCol, gridCol + 3, 3 * gridCol + 6]:
                        # Mark the full column as invalid locations.
                        possibilityGridBox[subGridCol] = 0
                        possibilityGridBox[subGridCol + 3] = 0
                        possibilityGridBox[subGridCol + 6] = 0

        gridArray = addCalculatedValues(gridArray, possibilityGrid, i)

    if checkComplete(gridArray) is False and count < 10:
        calculationPass(gridArray, count + 1)
    
    return gridArray



def addCalculatedValues(gridArray, possibilityGrid, number):
    for gridNumber, grid in enumerate(possibilityGrid):
        try:
            if grid.count(1) is 1:
                gridArray[gridNumber][grid.index(1)] = number
        except ValueError:
            continue

    return gridArray

def checkComplete(gridArray):

    isComplete = True

    for grid in gridArray:
        if grid.count(0) >= 1:
            isComplete = False
            break

    return isComplete

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

    for i in range(0, 3):
        for j in range(0, 3):
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

def getPossibilityGrid(gridArray):
    possibilityGrid = [
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

    # Already occupied locations are not valid locations.
    for index, grid in enumerate(gridArray):
        for location, value in enumerate(grid):
            if value is not 0:
                possibilityGrid[index][location] = 0;

    return possibilityGrid

def validate(values):
    validated = True
    #
    # errors = []
    #
    # for gridNumber, grid in enumerate(values):
    #     gridErrors = {}
    #     for gridPosition, value in enumerate(grid):
    #         if value.toInt()[1] is False:
    #             gridErrors[gridPosition] = ('value must be numeric')
    #
    #     errors.append(gridErrors)
    #
    # for gridErrors in errors:
    #     if len(gridErrors) is not 0:
    #         return errors

    #return []


    print "validation success"

    return validated

def formatValues(values):
    """format values into an array of integers, input values as immutable"""

    gridValues = []

    for box in values:
        subValues = []
        for valueObj in box:
            subValue = str(valueObj)

            subValues.append(int(subValue) if subValue != '' else 0)

        gridValues.append(subValues)

    return gridValues
