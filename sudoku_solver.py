import sys
import math
from PyQt4 import QtGui, QtCore
import sudoku_logic

class MainWindow(QtGui.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        self.wrapper = Wrapper(self)

        self.resize(800, 750)
        self.move(50, 50)
        self.setWindowTitle('SudokuSolverPy v0.1')
        self.show()

class Wrapper(QtGui.QFrame):

    messages = {
        'title' : 'Sudoku Solver',
        'infoLabel' : 'Enter your sudoku numbers into the boxes below and click solve!',
        'submitButtonLabel' : 'Solve!'
    }
    width  = 600
    height = 670

    def __init__(self, parent):
        super(Wrapper, self).__init__(parent)

        self.initWrapper()

    def initWrapper(self):

        print "Begin"

        self.board = Board(self)
        self.createLabels()

        self.submit = QtGui.QPushButton(self.messages['submitButtonLabel'], self)
        self.submit.setObjectName('submit_button')
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.resize(200, 50)
        self.submit.move(200, 600)

        QtCore.QObject.connect(
            self.submit,
            QtCore.SIGNAL('clicked()'),
            self.board.calculate
        )

        self.resize(self.width, self.height)
        self.move(100, 50)

        stylesheetFile = open('styles.qss', 'r')
        styles = stylesheetFile.read()

        self.setStyleSheet(styles)

    def createLabels(self):

        self.title = QtGui.QLabel(self.messages['title'], self)
        self.title.setObjectName('frame_title')
        self.title.resize(self.width - 40, 24)
        self.title.move(20, 20)

        #FIXME line height
        blockFormat = QtGui.QTextBlockFormat()
        blockFormat.setLineHeight(30, QtGui.QTextBlockFormat.LineDistanceHeight)

        self.infoLabel = QtGui.QTextEdit(self.messages['infoLabel'], self)
        self.infoLabel.setObjectName('frame_info_label')
        self.infoLabel.setWordWrapMode(True)
        self.infoLabel.setReadOnly(True)
        self.infoLabel.document().objectForFormat(blockFormat)
        self.infoLabel.resize(self.width - 40, 50)
        self.infoLabel.move(20, 50)

class Board(QtGui.QFrame):

    width  = 480
    height = 480

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.initBoard()

    def initBoard(self):

        self.puzzleBlocks = []

        self.setObjectName('puzzle_board')
        self.resize(self.width + 2, self.height + 2)
        self.move(60, 100)

        self.createPuzzleGrid()

    def createPuzzleGrid(self):

        for i in range(0, 9):
            block = QtGui.QFrame(self)
            block.setObjectName('puzzle_grid_%d' % i)
            block.setProperty('class', 'puzzle_grid')
            block.resize((self.width / 3), (self.height / 3))
            block.move(
                ((i % 3) * self.width / 3) + 1,
                (math.floor(i / 3) * self.height / 3) + 1
            )

            self.puzzleBlocks.append(block)

            for j in range(0, 9):
                numberInput = QtGui.QLineEdit(block)
                numberInput.setObjectName('puzzle_input_%d%d' % (i, j))
                numberInput.setProperty('class', 'puzzle_input')
                numberInput.setMaxLength(1)
                numberInput.setAlignment(QtCore.Qt.AlignHCenter)
                numberInput.resize(((self.width - 3) / 9), ((self.height - 3) / 9))
                numberInput.move(
                    (j % 3) * self.width / 9 + 1,
                    math.floor(j / 3) * self.height / 9 + 1
                )

    def calculate(self):
        calcValue = sudoku_logic.calculate(self.getValues())

    def getValues(self):
        values = []

        for block in self.puzzleBlocks:
            numberInputs = block.findChildren(QtGui.QLineEdit)
            blockValues = []

            for numberInput in numberInputs:
                blockValues.append(numberInput.text())

            values.append(blockValues)

        return values


def main():

    app = QtGui.QApplication(sys.argv)
    sudokuSolver = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
