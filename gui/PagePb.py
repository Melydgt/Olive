from .ressources import PageTemplate

class PagePb(PageTemplate):
    def __init__(self, config):
        super().__init__(config, title="Contenu de Page PB", has_filters=True)
