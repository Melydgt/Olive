from config.config import CONFIG
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QScrollArea, QLabel, QTextEdit, QPushButton, QComboBox


class PageTemplate(QWidget):
    def __init__(self, config, title="Contenu", has_filters=True):
        super().__init__()
        self.config = config
        self._content_layout = None  # Ajout ici
        layout = QVBoxLayout()

        if has_filters:
            layout.addWidget(self.create_filter_bar())
        layout.addWidget(self.create_scrollable_content(title))

        self.setLayout(layout)

    def create_filter_bar(self):
        filter_bar = QWidget()
        filter_bar.setStyleSheet(f"""
            background-color: {self.config["style"]["filter_bar"]};
        """)
        filter_bar.setFixedHeight(self.config["style"]["filter_bar_height"])
        filter_layout = QHBoxLayout()
        for _ in range(4):
            combobox = QComboBox()
            combobox.addItems(self.config["texts"][f"filter_options{_+1}"])
            combobox.setStyleSheet(f"""
                font-size: {self.config['style']['font_size']['filter1']};
            """)
            filter_layout.addWidget(combobox)
        filter_bar.setLayout(filter_layout)
        return filter_bar

    def create_scrollable_content(self, title):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_widget.setStyleSheet(f"""
            background-color: {self.config["style"]["content_bg"]};
        """)
        self._content_layout = QVBoxLayout(content_widget)

        # Contenu par défaut, peut être remplacé
        self._content_layout.addWidget(QLabel(title))

        scroll.setWidget(content_widget)
        return scroll

    def get_content_layout(self):
        return self._content_layout


class Header1(QWidget):
    def __init__(self):
        super().__init__()
        title = CONFIG["texts"]["header1_title"]
        layout = QHBoxLayout()
        label = QLabel(f"<b>{title}</b>")
        arrow = QLabel("▼")
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(arrow)
        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["header_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["header_background"]};
            border: {CONFIG["style"]["header_border"]};
            color: {CONFIG['style']['header_text_color']};
            font-size: {CONFIG['style']['font_size']['header1']};
            padding: 10px;
        """)


class Header2(QWidget):
    def __init__(self):
        super().__init__()
        title = CONFIG["texts"]["header2_title"]
        layout = QVBoxLayout()
        label = QLabel(f"<b>{title}</b>")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["header_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["header_background"]};
            border: {CONFIG["style"]["header_border"]};
            color: {CONFIG['style']['header_text_color']};
            font-size: {CONFIG['style']['font_size']['header1']};
            padding: 0px;
        """)


class Header3(QWidget):
    def __init__(self):
        super().__init__()
        left = CONFIG["texts"]["header3_left"]
        right = CONFIG["texts"]["header3_right"]
        layout = QHBoxLayout()
        layout.addWidget(QLabel(f"<b>{left}</b>"))
        layout.addSpacing(30)
        layout.addWidget(QLabel(f"<b> | </b>"))
        layout.addStretch()
        layout.addWidget(QLabel(f"<b>{right}</b>"))
        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["header_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["header_background"]};
            border: {CONFIG["style"]["header_border"]};
            color: {CONFIG['style']['header_text_color']};
            font-size: {CONFIG['style']['font_size']['header1']};
            padding: 10px;
        """)


class Footer1(QWidget):
    def __init__(self):
        super().__init__()
        quote = CONFIG["texts"]["footer1_quote"]
        total = CONFIG["texts"]["footer1_total"]
        layout = QHBoxLayout()
        quote_label = QLabel(f"<b style='color:red;'>{quote}</b>")
        total_label = QLabel(f"<span>{total}</span>")
        layout.addWidget(quote_label)
        layout.addStretch()
        layout.addWidget(total_label)
        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["footer_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["footer_background"]};
            border: {CONFIG["style"]["footer_border"]};
            color: {CONFIG['style']['footer_text_color']};
            font-size: {CONFIG['style']['font_size']['footer1']};
            padding: 10px;
        """)


class Footer2(QWidget):
    def __init__(self):
        super().__init__()
        quote = CONFIG["texts"]["footer2_quote"]
        action = CONFIG["texts"]["footer2_action"]
        layout = QHBoxLayout()
        quote_label = QLabel(f"<b style='color:red;'>{quote}</b>")
        action_label = QLabel(f"<b>{action}</b>")
        layout.addWidget(quote_label)
        layout.addStretch()
        layout.addWidget(action_label)
        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["footer_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["footer_background"]};
            border: {CONFIG["style"]["footer_border"]};
            color: {CONFIG['style']['footer_text_color']};
            font-size: {CONFIG['style']['font_size']['footer1']};
            padding: 10px;
        """)
