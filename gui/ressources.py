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
        label = QLabel(f"{title}")
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
            font-weight: bold; 
            padding: 10px;
        """)


class Header2(QWidget):
    def __init__(self):
        super().__init__()
        title = CONFIG["texts"]["header2_title"]
        layout = QVBoxLayout()
        label = QLabel(f"{title}")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["header_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["header_background"]};
            border: {CONFIG["style"]["header_border"]};
            color: {CONFIG['style']['header_text_color']};
            font-size: {CONFIG['style']['font_size']['header1']};
            font-weight: bold; 
            padding: 0px;
        """)


class Header3(QWidget):
    def __init__(self):
        super().__init__()
        left = CONFIG["texts"]["header3_left"]
        right = CONFIG["texts"]["header3_right"]
        layout = QHBoxLayout()
        layout.addWidget(QLabel(f"{left}"))
        layout.addStretch()
        layout.addWidget(QLabel(f"|"))
        layout.addStretch()
        layout.addWidget(QLabel(f"{right}"))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["header_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["header_background"]};
            border: {CONFIG["style"]["header_border"]};
            color: {CONFIG['style']['header_text_color']};
            font-size: {CONFIG['style']['font_size']['header1']};
            font-weight: bold; 
            padding: 10px;
        """)


class Footer1(QWidget):
    def __init__(self):
        super().__init__()
        quote = CONFIG["texts"]["footer1_quote"]
        total = CONFIG["texts"]["footer1_total"]
        layout = QHBoxLayout()
        quote_label = QLabel(f"{quote}")
        total_label = QLabel(f"{total}")
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
            font-weight: bold; 
            padding: 10px;
        """)


class Footer2(QWidget):
    def __init__(self):
        super().__init__()
        quote = CONFIG["texts"]["footer2_quote"]
        action = CONFIG["texts"]["footer2_action"]
        layout = QHBoxLayout()
        quote_label = QLabel(f"{quote}")
        action_label = QLabel(f"{action}")
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
            font-weight: bold; 
            padding: 10px;
        """)


class Row1(QWidget):
    def __init__(self, ticket_jira):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel(f"<b>{ticket_jira.key} | {ticket_jira.fields.summary}</b>"))
        layout.addStretch()
        layout.addWidget(QLabel(ticket_jira.fields.assignee))
        layout.addWidget(QLabel(str(ticket_jira.fields.labels)))
        layout.addWidget(QLabel(ticket_jira.fields.status))
        layout.addWidget(QLabel("Manquant : ..."))
        layout.addWidget(QLabel("Surplus : ..."))
        layout.addWidget(QPushButton("Résoudre"))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["row1_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["row1_background"]};
            border-bottom: {CONFIG["style"]["row1_border"]};
            color: {CONFIG['style']['row1_text_color']};
            font-size: {CONFIG['style']['font_size']['content1']};
            padding: 10px;
        """)


class Row2(QWidget):
    def __init__(self, ticket_ipmp):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel(f"<b>{ticket_ipmp.id} | {ticket_ipmp.Titre}</b>"))
        layout.addStretch()
        layout.addWidget(QLabel(ticket_ipmp.Responsable))
        layout.addWidget(QLabel("Réel / Estimé"))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["row2_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["row2_background"]};
            border-bottom: {CONFIG["style"]["row2_border"]};
            color: {CONFIG['style']['row2_text_color']};
            font-size: {CONFIG['style']['font_size']['content1']};
            padding: 10px;
        """)


class Row3(QWidget):
    def __init__(self, ticket_jira):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel(f"<b>{ticket_jira.key} | {ticket_jira.fields.summary}</b>"))
        layout.addStretch()
        layout.addWidget(QLabel(ticket_jira.fields.assignee))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["row2_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["row2_background"]};
            border-bottom: {CONFIG["style"]["row2_border"]};
            color: {CONFIG['style']['row2_text_color']};
            font-size: {CONFIG['style']['font_size']['content1']};
            padding: 10px;
        """)


class Row4(QWidget):
    def __init__(self, ticket_ipmp):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel(f"<b>{ticket_ipmp.id} | {ticket_ipmp.Titre}</b>"))
        layout.addStretch()
        layout.addWidget(QLabel(ticket_ipmp.Responsable))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["row2_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["row2_background"]};
            border-bottom: {CONFIG["style"]["row2_border"]};
            color: {CONFIG['style']['row2_text_color']};
            font-size: {CONFIG['style']['font_size']['content1']};
            padding: 10px;
        """)


class Row5(QWidget):
    def __init__(self, ticket_ipmp):
        super().__init__()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel(f"<b>{ticket_ipmp.id} | {ticket_ipmp.Titre}</b>"))
        layout.addStretch()
        layout.addWidget(QLabel(ticket_ipmp.Responsable))
        layout.addWidget(QLabel("Livré 🤔"))

        self.setLayout(layout)
        self.setFixedHeight(CONFIG["style"]["row2_height"])
        self.setStyleSheet(f"""
            background-color: {CONFIG["style"]["row2_background"]};
            border-bottom: {CONFIG["style"]["row2_border"]};
            color: {CONFIG['style']['row2_text_color']};
            font-size: {CONFIG['style']['font_size']['content1']};
            padding: 10px;
        """)
