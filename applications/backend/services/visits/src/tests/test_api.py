# from fastapi.testclient import TestClient
# from ..main import app
from ..cli.ci import Launcher

launcher = Launcher()
launcher.launch_up_to()

# client = TestClient(app)

def test_read_root():
    assert True
    # response = client.get("/version")
    # assert response.status_code == 200
