from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tickets import get_open_tickets, get_ticket, create_ticket, assign_ticket

app = FastAPI()

tickets = [
    {
        "id": 1,
        "customer": "Sam",
        "subject": "Cannot log in",
        "priority": "normal",
        "status": "open",
    },
    {
        "id": 2,
        "customer": "Mill",
        "subject": "Missing file",
        "priority": "high",
        "status": "open",
    },
    {
        "id": 3,
        "customer": "Arthur",
        "subject": "Password reset",
        "priority": "low",
        "status": "closed",
    },
]

class TicketCreate(BaseModel):
    customer: str
    subject: str
    priority: str= "normal"

class TicketAssignment(BaseModel):
    agent: str

@app.patch("/tickets/{ticket_id}/assignment")
def update_assignment(ticket_id: int, assignment: TicketAssignment):

    try:
        get_ticket(tickets, ticket_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    
    try:
        return assign_ticket(tickets, ticket_id, assignment.agent)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@app.get("/tickets")
def list_open_tickets():
    return get_open_tickets(tickets)

@app.get("/tickets/{ticket_id}")
def retrieve_ticket(ticket_id: int):
    try:
        return get_ticket(tickets, ticket_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

@app.post("/tickets", status_code=201)
def add_ticket(ticket: TicketCreate):
    try:
        return create_ticket(
            tickets,
            ticket.customer,
            ticket.subject,
            ticket.priority,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))    