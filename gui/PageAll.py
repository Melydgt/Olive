from .ressources import PageTemplate


class PageAll(PageTemplate):
    def __init__(self, config):
        super().__init__(config, title="Contenu de Page All", has_filters=True)
