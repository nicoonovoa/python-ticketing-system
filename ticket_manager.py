from ticket import Ticket

class TicketManager:
    def __init__(self):
        self._tickets = [] 
        self._next_id = 1

    def list_tickets(self):
        return self._tickets.copy()
    
    def create_ticket(self, title, description, priority):
        ticket = Ticket(self._next_id, title, description, priority)
        self._tickets.append(ticket)
        self._next_id += 1
        return ticket

    def get_ticket(self, id):
        for ticket in self._tickets:
            if ticket.id == id:
                return ticket