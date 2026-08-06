# Python Ticketing System

## Description

Python Ticketing System is a project that I created to develop my programming skills and learn more about Python. The project represents a simple system where users can report a problem by creating a ticket with a title, a short description and a priority.

## Current Features

- Create a ticket with an ID, title, description, priority and status.
- Remove unnecessary spaces from ticket information.
- Validate that the title is not empty.
- Validate ticket priorities using low, medium or high.
- Change a ticket's priority.
- Close and reopen tickets.

## Project Structure

- `main.py`: will be the entry point of the application and will allow users to access the project's functions.
- `storage.py`: will be responsible for saving and loading tickets.
- `ticket_manager.py`: will manage multiple tickets and connect the main application with the `Ticket` class.
- `ticket.py`: contains the `Ticket` class and its validation, priority and status methods.

## How to Run

1. Make sure Python is installed.
2. Clone or download the repository.
3. Open a terminal inside the project folder.
4. Run:

```bash
python main.py
```

## Roadmap

- [x] Implement the basic `Ticket` class.
- [x] Add ticket priority validation.
- [x] Add methods to close and reopen tickets.
- [x] Validate empty ticket descriptions.
- [ ] Implement the `TicketManager` class.
- [ ] Assign unique ticket IDs automatically.
- [ ] Add an interactive command-line interface to `main.py`.
- [ ] Save and load tickets using `storage.py`.
- [ ] Add automated tests.