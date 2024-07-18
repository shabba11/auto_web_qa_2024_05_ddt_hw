from datetime import datetime

import pytest


class TestPostResourceRequests:

    @pytest.mark.parametrize("cost",
                             (10.0, 20.1, 30, 40.23),
                             ids=["cost=10.0", "cost=20.1", "cost=30", "cost=40.23"])
    def test_post_resource_requests_required_params_ok(self, client, resource, cost):
        data = {"project_tasks_resource_id": resource,
                "volume": 10.0,
                "cost": cost,
                "needed_at": int(datetime.now().timestamp())}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        expected_data = response.json()
        for key in data.keys():
            assert data[key] == expected_data[key]

    @pytest.mark.parametrize("is_over_budget",
                             (True, False),
                             ids=["is_over_budget=True", "is_over_budget=False"])
    def test_post_resource_requests_is_over_budget_ok(self, client, resource, is_over_budget):
        data = {"project_tasks_resource_id": resource,
                "volume": 10,
                "cost": 10,
                "needed_at": int(datetime.now().timestamp()),
                "is_over_budget": is_over_budget}

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 201

        expected_data = response.json()
        for key in data.keys():
            assert data[key] == expected_data[
                key], f"{key} не равен переданному результату {data[key]} != {expected_data[key]}"

    @pytest.mark.parametrize("param, message",
                             (("project_tasks_resource_id", 'Ресурс'),
                              ("volume", 'Количество'),
                              ("cost", 'Цена, шт'),
                              ("needed_at", 'Дата востребования')),
                             ids=["project_tasks_resource_id=None", "volume=None", "cost=None", "needed_at=None"])
    def test_post_resource_requests_required_params_fault(self, client, resource, param, message):
        data = {"project_tasks_resource_id": resource,
                "volume": 10,
                "cost": 10,
                "needed_at": int(datetime.now().timestamp())}

        data.pop(param)

        response = client.post_projects_resource_request(data=data)
        assert response.status_code == 422

        expected_data = response.json()[0]
        assert expected_data['message'] == f'Необходимо заполнить «{message}».'
