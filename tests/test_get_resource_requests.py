import pytest

from gectaro_http_client import GectaroHttpClient
from response_models import ResourceRequestResponse


class TestGetResourceRequest:

    def test_get_resource_requests_ok(self, client):
        response = client.get_projects_resource_requests()
        assert response.status_code == 200
        ResourceRequestResponse(project_tasks=response.json())

    def test_get_resource_requests_unauthorized_fault(self):
        client = GectaroHttpClient(base_url="https://api.gectaro.com", token="01234")
        response = client.get_projects_resource_requests()
        assert response.status_code == 401

    @pytest.mark.parametrize(
        "project_id, status_code",
        ((1234, 403), (0, 404), (-1234, 404), (1234567890, 404)),
        ids=["project_id='No access",
             "project_id='Not available'",
             "project_id='Not available'",
             "project_id='Not available'"])
    def test_get_resource_requests_non_existent_project(self, client, project_id, status_code):
        client.project_id = project_id
        response = client.get_projects_resource_requests()

        assert response.status_code == status_code
