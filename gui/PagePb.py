from .ressources import (PageTemplate,
                         Header1,
                         Header2,
                         Header3,
                         Footer1,
                         Footer2,
                         Row1,
                         Row2,
                         Row3,
                         Row4,
                         Row5)
from DataClasses.TicketJira import TicketJira
from DataClasses.TicketIPMP import TicketIPMP

from PyQt5.QtWidgets import QLabel


class PagePb(PageTemplate):
    def __init__(self, config):
        super().__init__(config, title="", has_filters=True)

        layout = self.get_content_layout()

        self.setStyleSheet(f"""
            font-size: {self.config['style']['font_size']['content1']};
        """)

        ticket_jira_test = TicketJira(
            id="123",
            key="JIRA-123",
            assignee="John Doe",
            comment="Test comment",
            description="Test description",
            issuetype="Bug",
            labels=["test", "bug"],
            reporter="Jane Doe",
            resolution="Fixed",
            status="Open",
            summary="Test summary"
        )
        ticket_ipmp_test = TicketIPMP(
            id="456",
            Titre="Test Title",
            Projet="Test Project",
            Emetteur="John Doe",
            Responsable="Jane Doe",
            Description="Test description",
            Type_de_Ticket="Bug",
            Activite_de_planning="Test activity",
            Critere_de_complexite="Test complexity",
            Etat="Open",
            N_est_pas_bon_du_premier_coup="No",
            Date_acceptation="2023-10-01",
            Acceptation="Accepted",
            Travail_estime="5h",
            Travail_reel="3h",
            Heure_de_fin="2023-10-02 17:00:00",
            Clos="No",
            Resultat="Test result",
            Date_de_facturation="2023-10-03",
            Echeance_prevue="2023-10-04",
            hyperlien="http://example.com"
        )

        layout.addWidget(Header1())
        layout.addWidget(QLabel("Contenu spécifique à Row1"))
        layout.addWidget(Row1(ticket_jira_test))
        layout.addWidget(QLabel("Contenu spécifique à Row2"))
        layout.addWidget(Row2(ticket_ipmp_test))
        layout.addWidget(QLabel("Contenu spécifique à Row3"))
        layout.addWidget(Row3(ticket_jira_test))
        layout.addWidget(QLabel("Contenu spécifique à Row4"))
        layout.addWidget(Row4(ticket_ipmp_test))
        layout.addWidget(QLabel("Contenu spécifique à Row5"))
        layout.addWidget(Row5(ticket_ipmp_test))
        layout.addWidget(Header2())
        layout.addWidget(Header3())

        layout.addWidget(Footer1())
        layout.addWidget(Footer2())
