from pytest_pulse import step

class BaseAPI:
    def __init__(self, context_or_page):
        self.context_or_page = context_or_page

    def _get_request_context(self, request_setup):
        if request_setup is not None:
            return request_setup
        if hasattr(self.context_or_page, "request"):
            return self.context_or_page.request
        return self.context_or_page

    @step("Get response")
    def get_response(self, request_setup=None, url=None, headers=None, queryParams=None):
        request = self._get_request_context(request_setup)
        response = request.get(url, headers=headers, params=queryParams)
        if response.status != 200:
            print(f"GET Failed: {response.status} - {response.text()}")
        assert response.status == 200
        return response.json()

    @step("Post response")
    def post_response(self, request_setup=None, url=None, headers=None, data=None):
        request = self._get_request_context(request_setup)
        response = request.post(url, headers=headers, data=data)
        if response.status not in [200, 201]:
            print(f"POST Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201]
        return response.json()

    @step("Delete response")
    def delete_response(self, request_setup=None, url=None, headers=None):
        request = self._get_request_context(request_setup)
        response = request.delete(url, headers=headers)
        if response.status not in [200, 202, 204]:
            print(f"DELETE Failed: {response.status} - {response.text()}")
        assert response.status in [200, 202, 204]
        try:
            return response.json()
        except:
            return {}

    @step("Put response")
    def put_response(self, request_setup=None, url=None, headers=None, data=None):
        request = self._get_request_context(request_setup)
        response = request.put(url, headers=headers, data=data)
        if response.status not in [200, 201, 204]:
            print(f"PUT Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201, 204]
        return response.json()

    @step("Patch response")
    def patch_response(self, request_setup=None, url=None, headers=None, data=None):
        request = self._get_request_context(request_setup)
        response = request.patch(url, headers=headers, data=data)
        if response.status not in [200, 201]:
            print(f"PATCH Failed: {response.status} - {response.text()}")
        assert response.status in [200, 201]
        return response.json()
