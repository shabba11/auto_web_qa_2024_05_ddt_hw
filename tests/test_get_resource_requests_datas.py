from gectaro_http_client import GectaroHttpClient
from response_models import ResourceRequestResponse


class TestGetResourceRequestsDatas:

    def test_get_resource_requests_ok(self, client):
        response = client.get_projects_resources_request_datas()
        assert response.status_code == 200
        ResourceRequestResponse(project_tasks=response.json())

    def test_get_resource_requests_unauthorized_fault(self):
        client = GectaroHttpClient(base_url="https://api.gectaro.com", token="01234")
        response = client.get_projects_resources_request_datas()
        assert response.status_code == 401

    def test_get_resource_requests_non_existent_project(self, client):
        client.company_id = 1234567890
        response = client.get_projects_resources_request_datas()

        assert response.status_code == 400
