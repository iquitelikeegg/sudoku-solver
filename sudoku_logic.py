""" This is the logic component for the sudoku solver """

def calculate(puzzle):
    errors = validate(puzzle)

    if len(errors) is not 0:
        print "blah"

def validate(puzzle):
    errors = []

    for gridNumber, grid in enumerate(puzzle):
        gridErrors = {}
        for gridPosition, value in enumerate(grid):
            if value.toInt()[1] is False:
                gridErrors[gridPosition] = ('value must be numeric')

        errors.append(gridErrors)

    for gridErrors in errors:
        if len(gridErrors) is not 0:
            return errors

    return []
