import sys
from PyQt5.QtWidgets import QApplication
import MyWidgets
def main():
    app = QApplication(sys.argv)
    MainWin=MyWidgets.Mwin()
    MainWin.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()