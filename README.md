# Ticket Service

This is a small support ticket API built with Python and FastAPI.

I built this project to practise separating application logic from API routes,
validating input and writing automated tests. 

## Features

- Create tickets with a customer, subject and priority.
- Retrieve a ticket by ID.
- List open tickets by priority, then ID.
- Assign or reassign an agent to an open ticket.
- Reject invalid requests with error messages.

The Python code also supports closing tickets, but this is not yet
available through an API endpoint.

## Setup

Requires Python 3.13. The commands below are for Windows PowerShell.

From the project folder:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the API

```powershell
.\.venv\Scripts\python.exe -m uvicorn api:app --reload
```

Open http://127.0.0.1:8000/docs to try the endpoints using the
interactive API documentation.

## Run the tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Tests cover ticket creation, validation, sorting, assignment, closing
and selected API responses.

## Current limitations

- Tickets are stored in memory. Changes are lost when the application restarts.
- There is no authentication.
- This is a learning project, not a production service.

## Next steps

- Add persistent storage using SQLite.
- Include the existing close ticket function through the API.