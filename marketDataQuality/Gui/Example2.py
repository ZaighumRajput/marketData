'''
Closing windows & Message box

'''
import sys
from PyQt4 import QtGui, QtCore

class Example2(QtGui.QWidget):
    
    def __init__(self):
        super(Example2, self).__init__()

        self.initUI()

    def initUI(self):

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        

        self.center()
        self.setWindowTitle('Quit Button & Message Box')
        self.show()


    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           'Are you sure?', QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    

