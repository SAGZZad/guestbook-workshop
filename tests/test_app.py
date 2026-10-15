
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://guestbook:guestbook@localhost:5432/guestbook",
)

from fastapi.testclient import TestClient

from main import Message, app


def test_health():
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_message_model():
    message = Message(author="Test", text="Hello")

    assert message.author == "Test"
    assert message.text == "Hello"
