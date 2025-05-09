from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget
from .PagePb import PagePb
from .PageTemps import PageTemps
from .PageAll import PageAll
from .PageFactu import PageFactu

class MainWindow(QWidget):
    def __init__(self, config):
        super().__init__()
        self.setWindowTitle(config['texts']['window_title'])

        main_layout = QHBoxLayout(self)
        
        # Barre de navigation
        nav_widget = QWidget()
        nav_layout = QVBoxLayout(nav_widget)
        nav_widget.setStyleSheet(f"background-color: {config['colors']['navbar']};")
        nav_layout.setContentsMargins(10, 10, 10, 10)

        self.pages = QStackedWidget()
        pages_classes = [PagePb, PageTemps, PageAll, PageFactu]

        for i, page_class in enumerate(pages_classes):
            btn = QPushButton(config['texts']['pages'][i])
            btn.setStyleSheet(
                f"background-color: {config['colors']['navbar_button']}; color: {config['colors']['button_text']}; font-weight: bold; padding: 8px;"
            )
            btn.clicked.connect(lambda _, idx=i: self.pages.setCurrentIndex(idx))
            nav_layout.addWidget(btn)
            self.pages.addWidget(page_class(config))

        nav_layout.addStretch()
        main_layout.addWidget(nav_widget)
        main_layout.addWidget(self.pages)
