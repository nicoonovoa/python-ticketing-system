from ticket_manager import TicketManager


def test_new_manager_starts_without_tickets():
    manager = TicketManager()

    assert manager.list_tickets() == []

def test_create_ticket_assigns_id_and_stores_it():
    manager = TicketManager()

    ticket = manager.create_ticket(
        "No internet connection",
        "WiFi doesn't work on my computer",
        "medium"
    )
    assert ticket.id == 1
    assert manager.list_tickets()  == [ticket]

def test_create_multiple_tickets_assigns_consecutive_ids():
    manager = TicketManager()
    first_ticket = manager.create_ticket(
            "No internet connection",
            "WiFi doesn't work on my computer",
            "medium"
        )  
    second_ticket = manager.create_ticket(
            "Broken Keyboard",
            "My keyboard doesn't work",
            "high"
        )
    assert first_ticket.id == 1
    assert second_ticket.id == 2 

def test_get_ticket_by_id():
    manager = TicketManager()

    first_ticket = manager.create_ticket("No internet connection", "WiFi doesn't work on my computer", "medium")  
    second_ticket = manager.create_ticket("Broken Keyboard", "My keyboard doesn't work", "high")

    found_ticket = manager.get_ticket(second_ticket.id)
    assert found_ticket is second_ticket