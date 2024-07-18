from datetime import datetime


class TestDeleteResourceRequests:

    def test_delete_resource_requests_ok(self, client, resource):
        data = {"project_tasks_resource_id": resource,
                "volume": 10.0,
                "cost": 10.0,
                "needed_at": int(datetime.now().timestamp()),
                "is_over_budget": True}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        resource_id = response.json()["id"]
        new_response = client.delete_projects_resources_request_data(resource_id=resource_id)

        assert new_response.status_code == 204

    def test_delete_resource_requests_over_budget_false(self, client, resource):
        data = {"project_tasks_resource_id": resource,
                "volume": 10,
                "cost": 10,
                "needed_at": int(datetime.now().timestamp()),
                "is_over_budget": False}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        resource_id = response.json()["id"]
        new_response = client.delete_projects_resources_request_data(resource_id=resource_id)

        assert new_response.status_code == 422

    def test_delete_resource_requests_resource_id_fault(self, client, resource):
        response = client.delete_projects_resources_request_data(resource_id=0)

        assert response.status_code == 404

    def test_delete_resource_requests_resource_id_validation_fault(self, client, resource):
        response = client.delete_projects_resources_request_data(resource_id='abc')

        assert response.status_code == 404