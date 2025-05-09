from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QTextEdit
from PyQt5.QtCore import Qt

class PageFactu(QWidget):
    def __init__(self, config):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("<h2>Tickets ready to $$$</h2>")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content = QTextEdit()
        content.setPlainText("Contenu de la Page Factu\n" + "Lorem ipsum\n" * 30)
        content.setStyleSheet(f"background-color: {config['colors']['content_bg']};")
        scroll_area.setWidget(content)

        layout.addWidget(scroll_area)
        self.setLayout(layout)
