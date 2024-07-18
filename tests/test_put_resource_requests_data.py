from datetime import datetime


class TestPutResourceRequestsData:

    def test_put_resource_request_data(self, client, resource):
        data = {"project_tasks_resource_id": resource,
                "volume": 10.0,
                "cost": 10.0,
                "needed_at": int(datetime.now().timestamp())}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        project_id = response.json()["id"]
        new_data = {"cost": 15.0}

        new_response = client.put_projects_resource_request_data(project_id=project_id, data=new_data)
        assert new_response.status_code == 200

        data["cost"] = 15.0

        expected_data = new_response.json()
        for key in data.keys():
            assert data[key] == float(expected_data[
                key]), f"'{key}' не равен переданному результату {data[key]} != {expected_data[key]}"

    def test_put_resource_request_data_with_opt_data(self, client, resource):
        data = {"project_tasks_resource_id": resource,
                "volume": 10.0,
                "cost": 10.0,
                "needed_at": int(datetime.now().timestamp()),
                "is_over_budget": False}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        project_id = response.json()["id"]
        new_data = {"is_over_budget": True}

        new_response = client.put_projects_resource_request_data(project_id=project_id, data=new_data)
        assert new_response.status_code == 200

        all_data = {**data, **new_data}

        expected_data = new_response.json()
        for key in all_data.keys():
            assert all_data[key] == float(expected_data[
                key]), f"'{key}' не равен переданному результату {all_data[key]} != {expected_data[key]}"

    def test_put_resource_request_data_project_id_fault(self, client, resource):

        response = client.put_projects_resource_request_data(project_id=0, data={})
        assert response.status_code == 404

    def test_put_resource_request_data_with_not_valid_data(self, client, resource):
        data = {"project_tasks_resource_id": resource,
                "volume": 10.0,
                "cost": 10.0,
                "needed_at": int(datetime.now().timestamp()),
                "is_over_budget": False}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        project_id = response.json()["id"]
        new_data = {"is_over_budget": 5}

        new_response = client.put_projects_resource_request_data(project_id=project_id, data=new_data)
        assert new_response.status_code == 422
