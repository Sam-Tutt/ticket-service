def create_ticket(
    tickets: list[dict], 
    customer: str, 
    subject: str, 
    priority: str = "normal"
) -> dict:

    customer = customer.strip()
    subject = subject.strip()

    if not customer:
        raise ValueError("Customer cannot be empty.")
    if not subject:
        raise ValueError("Subject cannot be empty.")
    if priority not in ["low", "normal", "high"]:
        raise ValueError("Invalid priority.")

    highest_ticket_id = 0
    for ticket in tickets:
        if ticket["id"] > highest_ticket_id:
            highest_ticket_id = ticket["id"]

    ticket_id = highest_ticket_id + 1

    new_ticket = {
        "id": ticket_id,
        "customer": customer,
        "subject": subject,
        "priority": priority,
        "status": "open"
    }

    tickets.append(new_ticket)
                        

    return new_ticket

def close_ticket(tickets: list[dict], ticket_id: int) -> dict:
    for ticket in tickets:
        if ticket_id == ticket["id"]:
            ticket["status"] = "closed"
            return ticket
    raise ValueError("Ticket ID does not exist.")


def get_open_tickets(tickets: list[dict]) -> list[dict]:
    open_tickets = []
    priority_order = {
        "high": 0,
        "normal": 1,
        "low": 2,
    }

    for ticket in tickets:
        if ticket["status"] == "open":
            open_tickets.append(ticket)

    return sorted(open_tickets, key=lambda ticket: (priority_order[ticket["priority"]], ticket["id"]))


def assign_ticket(tickets: list[dict], ticket_id: int, agent: str) -> dict:
    agent = agent.strip()

    if not agent:
        raise ValueError("Agent cannot be empty.")

    found_ticket = None

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            found_ticket = ticket
            break

    if found_ticket is None:
        raise ValueError("Ticket not found.")

    if found_ticket["status"] == "closed":
        raise ValueError("Closed tickets cannot be assigned.")

    
    found_ticket["assigned_to"] = agent
    

    return found_ticket

def get_ticket(tickets: list[dict], ticket_id: int) -> dict:
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise ValueError("Ticket not found.")

