from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Working"}


def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "Working properly"}


def test_feedback_placeholder():
    response = client.get("/api/feedback")
    assert response.status_code == 200
    assert response.json() == {"message": "Placeholder_feedback"}


def test_name_with_query():
    response = client.get("/api/name", params={"name": "Smash"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome Smash"}


def test_name_default():
    response = client.get("/api/name")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome User"}