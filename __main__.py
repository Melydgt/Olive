import sys
from PyQt5.QtWidgets import QApplication
from config.config import load_config
from gui.MainWindow import MainWindow

if __name__ == "__main__":
    config = load_config()
    app = QApplication(sys.argv)
    window = MainWindow(config)
    window.resize(1000, 600)
    window.show()
    sys.exit(app.exec_())
