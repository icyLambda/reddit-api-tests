from requests.auth import HTTPBasicAuth

from core.RestClient import RestClient
from variables.data import BASE_URL, USER_AGENT


class AuthApi(RestClient):
    def login_by_password(self, script_id: str, secret_key: str, user_name: str, password: str,
                          user_agent: str = USER_AGENT, expected_code=None):
        """Аутентификация с помощью логина и пароля и получение bearer token"""

        user_auth = HTTPBasicAuth(username=script_id, password=secret_key)
        post_data = {"grant_type": "password", "username": user_name, "password": password}
        headers = {"User-Agent": user_agent}

        response = self._post(
            url=f"{BASE_URL}/api/v1/access_token",
            data=post_data,
            headers=headers,
            auth=user_auth,
            expected_codes=expected_code
        )

        return response.json()
