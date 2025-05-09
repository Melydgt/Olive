import sys
from gui.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
from config.config import CONFIG


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(CONFIG)
    window.resize(1000, 600)
    window.show()
    sys.exit(app.exec_())
