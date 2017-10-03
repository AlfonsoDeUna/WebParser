import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500, 345)
    w.move(400, 400)
    w.setWindowTitle('Web Parser')
    w.show()
    sys.exit(app.exec_())
