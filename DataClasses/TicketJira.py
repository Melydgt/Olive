class TicketJira:
    """
    CLASSE DE TEST UNIQUEMENT POUR L'AFFICHAGE.
    Class representing a Jira ticket. 
    """
    class TicketJira_fields:
        def __init__(self, assignee: str, comment: str, description: str, issuetype: str, labels: list[str], reporter: str, resolution: str, status: str, summary: str):
            self.assignee = assignee
            self.comment = comment
            self.description = description
            self.issuetype = issuetype
            self.labels = labels
            self.reporter = reporter
            self.resolution = resolution
            self.status = status
            self.summary = summary

    def __init__(self, id: str, key: str, assignee: str, comment: str, description: str, issuetype: str, labels: list[str], reporter: str, resolution: str, status: str, summary: str):
        self.id = id
        self.key = key
        self.fields = self.TicketJira_fields(
            assignee, comment, description, issuetype, labels, reporter, resolution, status, summary)

    def __str__(self):
        return f"TicketJira(id={self.id}, key={self.key}, fields={self.fields.__dict__})"
