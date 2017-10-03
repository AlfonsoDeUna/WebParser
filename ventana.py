import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
    webparser = QApplication(sys.argv)
    ventana = QWidget()
    ventana.resize(500, 345)
    ventana.move(400, 400)
    ventana.setWindowTitle('Web Parser')
    ventana.show()
    sys.exit(webparser.exec_())
