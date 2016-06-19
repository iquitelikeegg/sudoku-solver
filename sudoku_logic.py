""" This is the logic component for the sudoku solver """

import math, copy, time

def calculate(values):
    start = time.time() * 1000

    if validate(values) != True:
        """ Exit! """
        return

    puzzle = formatValues(values)

    calculationCount = 0

    calculatedArray = calculationPass(puzzle, calculationCount)

    end = time.time() * 1000;

    print "calculation in %d ms" % (end - start)

    return calculatedArray

def calculationPass(puzzle, count):
    previousPuzzle = copy.deepcopy(puzzle)
    rows           = getRows(puzzle)
    columns        = getColumns(puzzle)

    for i in range (1, 10):
        probGrid = getProbGrid(puzzle)

        puzzle = calcRowsAndCols(puzzle, rows, columns)

    if puzzle == previousPuzzle:
        # calcRowsAndCols is stuck
        # Try completing rows
        puzzle = completeRows(puzzle, rows, columns)
        puzzle = completeCols(puzzle, rows, columns)

    if not(checkComplete(puzzle)) and puzzle != previousPuzzle:
        return calculationPass(puzzle, count + 1)

    if not(checkComplete(puzzle)):
        print "failed to complete puzzle after %d passes" % (count + 1)
    else:
        print "completed in %d passes" % (count + 1)
    
    return puzzle

def calcRowsAndCols(puzzle, rows, columns):
    # Go through the rows.
    for i in range (1, 10):
        probGrid = getProbGrid(puzzle)

        # Go through the rows.
        for rowNumber, row in enumerate(rows):
            if i in row:
                # 0-2 the row the grid the [i] is in.
                gridRow = int(math.floor(rowNumber / 3))
                # 0-2 the row of [i] within the grid.
                subGridRow = rowNumber if rowNumber < 3 else (rowNumber % 3)

                for j, probGridBox in enumerate(probGrid):
                    # Is the possiblity grid box within the row of grids that [i] appears in?
                    if j in [3 * gridRow, 3 * gridRow + 1, 3 * gridRow + 2]:
                        # Mark the full row as invalid locations.
                        probGridBox[3 * subGridRow] = 0
                        probGridBox[3 * subGridRow + 1] = 0
                        probGridBox[3 * subGridRow + 2] = 0

                    try:
                        # Mark the grids that [i] appears in.
                        if j == int(3 * gridRow + math.floor(row.index(i) / 3)):
                            for k in range(0, 9):
                                probGridBox[k] = 0
                    except ValueError:
                        continue

        # Go through columns.
        for colNumber, col in enumerate(columns):
            if i in col:
                # 0-2 The column of the grid that [i] is in
                gridCol = int(math.floor(colNumber / 3))
                # 0-2 The column of [i] within the grid
                subGridCol = colNumber if colNumber < 3 else (colNumber % 3)

                for l, probGridBox in enumerate(probGrid):
                    if l in [gridCol, gridCol + 3, gridCol + 6]:
                        # Mark the full column as invalid locations.
                        probGridBox[subGridCol] = 0
                        probGridBox[subGridCol + 3] = 0
                        probGridBox[subGridCol + 6] = 0

                    try:
                        # Mark the grids that [i] appears in.
                        if l == int(3 * gridRow + math.floor(row.index(i) / 3)):
                            for m in range(0, 9):
                                probGridBox[m] = 0
                    except ValueError:
                        continue

        puzzle = addCalculatedValues(puzzle, probGrid, i)    

    return puzzle

def completeRows(puzzle, rows, columns):
    print "completing rows..."

    for rowNumber, row in enumerate(rows):
        missing = []
        emptyLocations = [i for i, value in enumerate(row) if value == 0]

        for n in range(1, 10):
            try:
                if isinstance(row.index(n), int):
                    continue
            except ValueError:
                missing.append(n)

        possibleResults = []

        for i in emptyLocations:
            potentialValues = []

            for m in missing:
                if not(findInColumn(columns, i, m)) \
                    and not(findInGrid(puzzle, int((math.floor(rowNumber / 3) * 3) + math.floor(i / 3)), m)) \
                :
                    potentialValues.append(m)

            if len(potentialValues) is 1:
                puzzle[int((math.floor(rowNumber / 3) * 3) + math.floor(i / 3))] \
                    [int(((rowNumber % 3) * 3) + (i % 3))] = potentialValues[0]

    return puzzle

def completeCols(puzzle, rows, columns):
    print "completing columns..."

    for colNumber, col in enumerate(columns):
        missing = []
        emptyLocations = [i for i, value in enumerate(col) if value == 0]

        for n in range(1, 10):
            try:
                if isinstance(col.index(n), int):
                    continue
            except ValueError:
                missing.append(n)

        possibleResults = []

        for i in emptyLocations:
            potentialValues = []

            for m in missing:
                if not(findInRow(rows, i, m)) \
                    and not(findInGrid(puzzle, int((math.floor(i / 3) * 3) + math.floor(colNumber / 3)), m)) \
                :
                    potentialValues.append(m)

            if len(potentialValues) is 1:
                puzzle[int((math.floor(i / 3) * 3) + math.floor(colNumber / 3))] \
                    [int(((i % 3) * 3) + (colNumber % 3))] = potentialValues[0]

    return puzzle

def findInGrid(puzzle, gridNumber, value):
    try:
        return isinstance(puzzle[gridNumber].index(value), int)
    except ValueError:
        return False

def findInColumn(columns, columnNumber, value):
    try:
        return isinstance(columns[columnNumber].index(value), int)
    except ValueError:
        return False

def findInRow(rows, rowNumber, value):
    try:
        return isinstance(rows[rowNumber].index(value), int)
    except ValueError:
        return False

def addCalculatedValues(puzzle, probGrid, number):
    for index, grid in enumerate(probGrid):
        try:
            if grid.count(1) is 1:
                puzzle[index][grid.index(1)] = number
        except ValueError:
            continue

    return puzzle

def checkComplete(puzzle):

    isComplete = True

    for grid in puzzle:
        if grid.count(0) >= 1:
            isComplete = False
            break

    return isComplete

def getRows(puzzle):
    rows = []

    for i in range(0, 3):
        for j in range(0, 3):
            row = []
            row.append(puzzle[3 * i][3 * j])
            row.append(puzzle[3 * i][3 * j + 1])
            row.append(puzzle[3 * i][3 * j + 2])
            row.append(puzzle[3 * i + 1][3 * j])
            row.append(puzzle[3 * i + 1][3 * j + 1])
            row.append(puzzle[3 * i + 1][3 * j + 2])
            row.append(puzzle[3 * i + 2][3 * j])
            row.append(puzzle[3 * i + 2][3 * j + 1])
            row.append(puzzle[3 * i + 2][3 * j + 2])

            rows.append(row)

    return rows

def getColumns(puzzle):
    columns = []

    for i in range(0, 3):
        for j in range(0, 3):
            column = []
            column.append(puzzle[i][j])
            column.append(puzzle[i][j + 3])
            column.append(puzzle[i][j + 6])
            column.append(puzzle[i + 3][j])
            column.append(puzzle[i + 3][j + 3])
            column.append(puzzle[i + 3][j + 6])
            column.append(puzzle[i + 6][j])
            column.append(puzzle[i + 6][j + 3])
            column.append(puzzle[i + 6][j + 6])

            columns.append(column)

    return columns

def getProbGrid(puzzle):
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
    for index, grid in enumerate(puzzle):
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

    puzzleValues = []

    for box in values:
        subValues = []
        for valueObj in box:
            subValue = str(valueObj)

            subValues.append(int(subValue) if subValue != '' else 0)

        puzzleValues.append(subValues)

    return puzzleValues
