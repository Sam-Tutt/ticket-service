import pytest
from fastapi.testclient import TestClient
import api


@pytest.fixture
def client(monkeypatch):
    fresh_tickets = [
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
            "status": "closed",
        },
    ]

    monkeypatch.setattr(api, "tickets", fresh_tickets)

    with TestClient(api.app) as test_client:
        yield test_client

def test_missing_ticket_returns_404(client):
    response = client.get("/tickets/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Ticket not found."
    }

def test_get_ticket_returns_200(client):
    response = client.get("/tickets/1")

    assert response.status_code == 200

    ticket = response.json()

    assert ticket["id"] == 1
    assert ticket["customer"] == "Sam"

def test_create_then_retrieve_ticket(client):
    response = client.post(
        "/tickets",
        json={
            "customer": "Lucy",
            "subject": "Cannot open attachment",
            "priority": "high",
        },
    )

    assert response.status_code == 201

    ticket = response.json()

    assert ticket["customer"] == "Lucy"
    assert ticket["subject"] == "Cannot open attachment"
    assert ticket["priority"] == "high"
    assert ticket["status"] == "open"

    ticket_id = ticket["id"]

    get_response = client.get(f"/tickets/{ticket_id}")

    assert get_response.status_code == 200
    assert get_response.json() == ticket

def test_assigning_closed_ticket_returns_400(client):
    response = client.patch(
        "/tickets/2/assignment",
        json={"agent": "Mill"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Closed tickets cannot be assigned."
    }