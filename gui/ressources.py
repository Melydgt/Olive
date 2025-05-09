from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QScrollArea, QTextEdit

class PageTemplate(QWidget):
    def __init__(self, config, title="Contenu", has_filters=True):
        super().__init__()
        self.config = config
        layout = QVBoxLayout()

        if has_filters:
            layout.addWidget(self.create_filter_bar())
        layout.addWidget(self.create_scrollable_content(title))

        self.setLayout(layout)

    def create_filter_bar(self):
        widget = QWidget()
        widget.setStyleSheet(f"background-color: {self.config['colors']['filter_bar']};")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(10, 10, 10, 10)
        for _ in range(4):
            combo = QComboBox()
            combo.addItems(["Item 1", "Item 2", "Item 3"])
            layout.addWidget(combo)
        return widget

    def create_scrollable_content(self, title):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content = QTextEdit()
        content.setPlainText(f"{title}\n" + "Lorem ipsum\n" * 30)
        content.setStyleSheet(f"background-color: {self.config['colors']['content_bg']};")
        scroll_area.setWidget(content)
        return scroll_area
