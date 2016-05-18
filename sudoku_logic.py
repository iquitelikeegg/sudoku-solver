""" This is the logic component for the sudoku solver """

def calculate(values):
    if validate(values) != True:
        """ Exit! """
        return

    


def validate(values):
    validated = True

    for box in values:
        for valueObj in box:
            print valueObj
            print "\n"
        print "\n"

    return validated
