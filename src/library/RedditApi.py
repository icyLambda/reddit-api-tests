from core.RestClient import RestClient

from variables.data import BASE_OAUTH_URL, USER_AGENT


class RedditApi(RestClient):
    def thread_search(self, subreddit: str, token: str, limit: int = 1, user_agent: str = USER_AGENT,
                      expected_code=None):
        params = {
            'limit': limit,
            'q': subreddit
        }

        headers = {"Authorization": f"bearer {token}", "User-Agent": user_agent}

        response = self._get(
            url=f'{BASE_OAUTH_URL}/search',
            params=params,
            headers=headers,
            expected_codes=expected_code
        )

        return response.json()

    def publish_comment(self, thread_id: str, comment: str, token: str, user_agent: str = USER_AGENT,
                        expected_code=None):
        params = {
            'thing_id': thread_id,
            'text': comment
        }

        headers = {"Authorization": f"bearer {token}", "User-Agent": user_agent}

        response = self._post(
            url=f'{BASE_OAUTH_URL}/api/comment',
            params=params,
            headers=headers,
            expected_codes=expected_code
        )

        return response.json()

    def remove_comment(self, comment_id: str, token: str, user_agent: str = USER_AGENT, expected_code=None):
        params = {
            'id': comment_id,
        }

        headers = {"Authorization": f"bearer {token}", "User-Agent": user_agent}

        response = self._post(
            url=f'{BASE_OAUTH_URL}/api/del',
            params=params,
            headers=headers,
            expected_codes=expected_code
        )

        return response.json()
