from .ressources import PageTemplate

class PageTemps(PageTemplate):
    def __init__(self, config):
        super().__init__(config, title="Contenu de Page Temps", has_filters=True)
