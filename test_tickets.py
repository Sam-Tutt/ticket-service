from tickets import create_ticket, close_ticket, get_open_tickets, assign_ticket
import pytest
from copy import deepcopy


def test_creates_first_ticket():
    tickets = []

    result = create_ticket(tickets, " Sam ", " Login problem ")

    expected = {
        "id": 1,
        "customer": "Sam",
        "subject": "Login problem",
        "priority": "normal",
        "status": "open",
    }

    assert result == expected
    assert tickets == [expected]

def test_ids_with_gaps():
    tickets = [
        {
            "id": 1,
            "customer": "Sam",
            "subject": "Login problem",
            "priority": "normal",
            "status": "open",
        },
        {
            "id": 4,
            "customer": "Mill",
            "subject": "Login problem",
            "priority": "normal",
            "status": "open",
        }
    ]

    result = create_ticket(tickets, "James", "Cannot find file.")

    expected = {
        "id": 5,
        "customer": "James",
        "subject": "Cannot find file.",
        "priority": "normal",
        "status": "open",
    }

    assert result == expected
    assert len(tickets) == 3
    assert tickets[-1] == expected

def test_invalid_customer():
    tickets = []

    with pytest.raises(ValueError):
        create_ticket(tickets, " ", "Help")

    assert tickets == []

def test_invalid_subject():
    tickets = []

    with pytest.raises(ValueError):
        create_ticket(tickets, "Sam", " ")

    assert tickets == []

def test_closing_ticket():
    tickets = [
        {
            "id": 5,
            "customer": "James",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
        }
    ]

    result = close_ticket(tickets, 5)

    expected = {
        "id": 5,
        "customer": "James",
        "subject": "Cannot find file.",
        "priority": "normal",
        "status": "closed",
    }

    assert result == expected
    assert tickets == [expected]

def test_get_open_tickets():
    tickets = [
        {
            "id": 8,
            "customer": "James",
            "subject": "Cannot find file.",
            "priority": "low",
            "status": "open",
        },
        {
            "id": 5,
            "customer": "Sam",
            "subject": "Cannot find file.",
            "priority": "high",
            "status": "open",
        },
        {
            "id": 2,
            "customer": "John",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "closed",
        },
        {
            "id": 3,
            "customer": "Bill",
            "subject": "Cannot find file.",
            "priority": "high",
            "status": "open",
        },
        {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
        }
    ]

    result = get_open_tickets(tickets)

    assert [ticket["id"] for ticket in result] == [3, 5, 6, 8]
    assert [ticket["id"] for ticket in tickets] == [8, 5, 2, 3, 6]

def test_assign_to_open_ticket():

    tickets = [
        {
           "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open", 
        }
    ]

    result = assign_ticket(tickets, 6, " Mill ")

    expected = {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
            "assigned_to": "Mill"
        }
    

    assert result == expected
    assert tickets == [expected]

def test_assign_ticket_to_assigned_ticket():
    tickets = [
        {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
            "assigned_to": "Mill"
        }
    ]

    result = assign_ticket(tickets, 6, "Sam")

    expected = {
        "id": 6,
        "customer": "Gregg",
        "subject": "Cannot find file.",
        "priority": "normal",
        "status": "open",
        "assigned_to": "Sam"
    }

    assert result == expected
    assert tickets == [expected]

def test_empty_agent_name():
    tickets = [
        {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
        }
    ]

    before = deepcopy(tickets)

    with pytest.raises(ValueError):
        assign_ticket(tickets, 6, " ")

    assert tickets == before

def test_ticket_not_found():
    tickets = [
        {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "open",
        }
    ]

    before = deepcopy(tickets)

    with pytest.raises(ValueError):
        assign_ticket(tickets, 1, "Mill")

    assert tickets == before


def test_assign_to_closed_ticket():
    tickets = [
        {
            "id": 6,
            "customer": "Gregg",
            "subject": "Cannot find file.",
            "priority": "normal",
            "status": "closed",
        }
    ]

    before = deepcopy(tickets)

    with pytest.raises(ValueError):
        assign_ticket(tickets, 6, "Mill")

    assert tickets == before
