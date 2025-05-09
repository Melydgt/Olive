from .ressources import PageTemplate, Header1, Header2, Footer1
from PyQt5.QtWidgets import QLabel


class PagePb(PageTemplate):
    def __init__(self, config):
        super().__init__(config, title="", has_filters=True)

        layout = self.get_content_layout()

        layout.addWidget(Header1())
        layout.addWidget(Header2())

        # Ton contenu spécifique ici
        layout.addWidget(QLabel("Contenu spécifique à PagePB"))
        self.setStyleSheet(f"""
            font-size: {self.config['style']['font_size']['content1']};
        """)

        layout.addWidget(Footer1())
