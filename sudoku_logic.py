""" This is the logic component for the sudoku solver """

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

        continue

def getRows(gridArray):
    rows = []

    for i in range(0, 2):
        for j in range(0, 2):
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
