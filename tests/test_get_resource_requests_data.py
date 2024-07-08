from datetime import datetime

import pytest


class TestResourceRequestsData:

    @pytest.mark.parametrize("resource_request_ids",
                             (True, False),
                             ids=["resource_request_ids exist", "resource_request_ids not_exist"])
    def test_get_resource_requests_data(self, client, resource, resource_request_ids):
        project_id = None

        if resource_request_ids:
            data = {"project_tasks_resource_id": resource,
                    "volume": 10,
                    "cost": 10,
                    "needed_at": int(datetime.now().timestamp())}

            response = client.post_projects_resource_request(data=data)
            assert response.status_code == 201

            project_id = response.json()["id"]

        get_resource_response = client.get_projects_resource_request_data(
            project_id=project_id if resource_request_ids else 0)
        assert get_resource_response.status_code == 200 if resource_request_ids else 404

    @pytest.mark.parametrize("cost",
                             (10.0, 20.1, 30, 40.23),
                             ids=["cost=10.0", "cost=20.1", "cost=30", "cost=40.23"])
    def test_get_resource_requests_data_ok(self, client, resource, cost):
        data = {"project_tasks_resource_id": resource,
                "volume": 10,
                "cost": cost,
                "needed_at": int(datetime.now().timestamp())}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        project_id = response.json()["id"]

        get_resource_response = client.get_projects_resource_request_data(project_id=project_id)
        expected_data = get_resource_response.json()

        assert get_resource_response.status_code == 200

        for key in data.keys():
            assert data[key] == expected_data[
                key], f"'{key}' не равен переданному результату {data[key]} != {expected_data[key]}"

    def test_get_resource_requests_data_page_not_found(self, client):
        get_resource_response = client.get_projects_resource_request_data(project_id='abc')
        assert get_resource_response.status_code == 404
