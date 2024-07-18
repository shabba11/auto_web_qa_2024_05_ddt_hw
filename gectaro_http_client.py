import requests


class GectaroHttpClient:

    def __init__(self, base_url, token, company_id="7323", project_id="85872"):
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.base_url = base_url
        self.project_id = project_id
        self.company_id = company_id

    def get_projects_resource_requests(self):
        response = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests")
        return response

    def post_projects_resources(self, data: dict):
        response = self.session.post(f"{self.base_url}/v1/projects/{self.project_id}/resources",
                                     json=data)
        return response

    def post_projects_resource_request(self, data):
        response = self.session.post(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests",
                                     json=data)
        return response

    def get_projects_resource_request_data(self, project_id):
        response = self.session.get(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{project_id}")
        return response

    def put_projects_resource_request_data(self, project_id, data):
        response = self.session.put(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{project_id}",
                                    json=data)
        return response

    def delete_projects_resources_request_data(self, resource_id):
        response = self.session.delete(f"{self.base_url}/v1/projects/{self.project_id}/resource-requests/{resource_id}")
        return response

    def get_projects_resources_request_datas(self):
        response = self.session.get(f"{self.base_url}/v1/companies/{self.company_id}/resource-requests")
        return response

