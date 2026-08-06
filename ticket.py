class Ticket:
    def __init__(self, ticket_id, title, description, priority):
        title = title.strip()
        description = description.strip()
        priority = priority.strip()
        if not description:
            raise ValueError("La descripción no puede estar vacía")
        priority = priority.lower()
        if priority not in ("high", "medium", "low"):
            raise ValueError("Prioridad no válida")
        if not title:
            raise ValueError("El título no puede estar vacío")
        self.id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "open"

    def change_priority(self, new_priority):
        new_priority = new_priority.strip()
        new_priority = new_priority.lower()
        if new_priority not in ("high", "medium", "low"):
            raise ValueError("Prioridad no válida")
        self.priority = new_priority

    def close(self):
        self.status = "closed"

    def reopen(self):
        self.status = "open"