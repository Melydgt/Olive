class TicketIPMP:
    """
    CLASSE DE TEST UNIQUEMENT POUR L'AFFICHAGE.
    Classe représentant un ticket IPMP.
    """

    def __init__(self, id: str, Titre: str, Projet: str, Emetteur: str, Responsable: str, Description: str, Type_de_Ticket: str, Activite_de_planning: str, Critere_de_complexite: str, Etat: str, N_est_pas_bon_du_premier_coup: str, Date_acceptation: str, Acceptation: str, Travail_estime: str, Travail_reel: str, Heure_de_fin: str, Clos: str, Resultat: str, Date_de_facturation: str, Echeance_prevue: str, hyperlien: str) -> None:
        self.id = id
        self.Titre = Titre
        self.Projet = Projet
        self.Emetteur = Emetteur
        self.Responsable = Responsable
        self.Description = Description
        self.Type_de_Ticket = Type_de_Ticket
        self.Activite_de_planning = Activite_de_planning
        self.Critere_de_complexite = Critere_de_complexite
        self.Etat = Etat
        self.N_est_pas_bon_du_premier_coup = N_est_pas_bon_du_premier_coup
        self.Date_acceptation = Date_acceptation
        self.Acceptation = Acceptation
        self.Travail_estime = Travail_estime
        self.Travail_reel = Travail_reel
        self.Heure_de_fin = Heure_de_fin
        self.Clos = Clos
        self.Resultat = Resultat
        self.Date_de_facturation = Date_de_facturation
        self.Echeance_prevue = Echeance_prevue
        self.hyperlien = hyperlien

    def __str__(self) -> str:
        return f"TicketIPMP(id={self.id}, Titre={self.Titre}, Projet={self.Projet}, Emetteur={self.Emetteur}, Responsable={self.Responsable}, Description={self.Description}, Type_de_Ticket={self.Type_de_Ticket}, Activite_de_planning={self.Activite_de_planning}, Critere_de_complexite={self.Critere_de_complexite}, Etat={self.Etat}, N_est_pas_bon_du_premier_coup={self.N_est_pas_bon_du_premier_coup}, Date_acceptation={self.Date_acceptation}, Acceptation={self.Acceptation}, Travail_estime={self.Travail_estime}, Travail_reel={self.Travail_reel}, Heure_de_fin={self.Heure_de_fin}, Clos={self.Clos}, Resultat={self.Resultat}, Date_de_facturation={self.Date_de_facturation}, Echeance_prevue={self.Echeance_prevue}, hyperlien={self.hyperlien})"
