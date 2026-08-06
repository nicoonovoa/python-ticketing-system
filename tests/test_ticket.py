import pytest
from ticket import Ticket


def test_create_valid_ticket():
    ticket = Ticket(1, "No internet connection", "WiFi doesn't work on my computer", "medium")
    assert ticket.id == 1
    assert ticket.title == "No internet connection"
    assert ticket.description == "WiFi doesn't work on my computer"
    assert ticket.priority == "medium"
    assert ticket.status == "open"


def test_reject_empty_title():
    with pytest.raises(ValueError):
        Ticket(1, "   ", "WiFi doesn't work on my computer", "medium")


def test_reject_empty_description():
    with pytest.raises(ValueError):
        Ticket(1, "No internet connection", "   ", "medium")


def test_reject_invalid_priority():
    with pytest.raises(ValueError):
        Ticket(1, "No internet connection", " WiFi doesn't work on my computer  ", "urgent")


def test_change_priority():
    ticket = Ticket(1, "No internet connection", "WiFi doesn't work on my computer", "medium")
    ticket.change_priority("  HIGH  ")
    assert ticket.priority == "high"


def test_close_and_reopen_ticket():
    ticket = Ticket(1, "No internet connection", "WiFi doesn't work on my computer", "medium")
    assert ticket.status == "open"
    ticket.close()
    assert ticket.status == "closed"
    ticket.reopen()
    assert ticket.status == "open"
def test_reject_invalid_new_priority():
    ticket = Ticket(1, "No internet connection", "WiFi doesn't work on my computer", "medium")
    with pytest.raises(ValueError):
        ticket.change_priority("urgent")