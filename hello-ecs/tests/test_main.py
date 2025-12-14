from app.main import read_root

def test_read_root():
    response = read_root()
    assert response["message"] == "Hello World from ECS"
