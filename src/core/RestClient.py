import json as jsn
from html import escape
from http import HTTPStatus

from requests import Response
from requests import Session

from core.built_in import built_in

_session = Session()


class RestClient:
    """REST-клиент."""

    __decoded_types = "text/", "application/json"
    __auto_format_content_type = "application/json"
    __json_indent_level = 2

    _default_headers = {"content-type": "application/json"}

    _success_codes = {
        HTTPStatus.OK,
        HTTPStatus.CREATED,
        HTTPStatus.ACCEPTED,
        HTTPStatus.NO_CONTENT,
    }

    @classmethod
    def __log_request(cls, response: Response):
        """Логирование запроса

        Возможно устанавливать уровень оповещений с помощью
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)

        :param response: http-ответ.
        """
        request = response.request
        request_headers = "\n".join(
            f"{header}: {header_value}"
            for header, header_value in request.headers.items()
        )

        if not request.body:
            request_body = None
        elif request.headers["Content-Type"].startswith(cls.__decoded_types):
            request_body = request.body.decode()
        else:
            request_body = "<encoded>"

        if request_body and request.headers.get("content-type", "").startswith(
                cls.__auto_format_content_type
        ):
            request_body = jsn.dumps(
                jsn.loads(request_body),
                ensure_ascii=False,
                indent=cls.__json_indent_level,
            )
        elif request_body:
            request_body = escape(request_body)

        response_headers = "\n".join(
            f"{header}: {header_value}"
            for header, header_value in response.headers.items()
        )
        response_body = response.text
        if response_body and response.headers.get("content-type", "").startswith(
                cls.__auto_format_content_type
        ):
            response_body = jsn.dumps(
                response.json(), ensure_ascii=False, indent=cls.__json_indent_level
            )
        elif response_body:
            response_body = escape(response_body)

        log = f"""<details>
        <summary>&gt;&gt;&gt; <b>{request.method}</b> {request.url}</summary>
        <div>{request_headers}</div>
        <pre>{request_body or '<empty>'}</pre>
        </details>
        <details>
        <summary>&lt;&lt;&lt; <b>{response.status_code}</b> {response.reason}</summary>
        <div>{response_headers}</div>
        <pre>{response_body}</pre>
        </details>
        """
        built_in.log(message=log, level="INFO", html=True)

    @classmethod
    def _headers(cls, headers: dict) -> dict:
        return cls._default_headers if headers is None else headers

    @classmethod
    def _expected_codes(cls, codes) -> set:
        """Приведение списка ожидаемых кодов к стандартному набору.

        :param codes: коды ответа.
        :return: Набор ожидаемых кодов ответа.
        """
        if codes is None:
            return cls._success_codes
        if isinstance(codes, (tuple, list, set)):
            return {*map(int, codes)}
        return {int(codes)}

    def _get(self, url: str, params=None, headers=None, auth=None, cookies=None, expected_codes=None) -> Response:
        """HTTP GET

        :param url: URL запроса.
        :param params: словарь параметров строки запроса.
        :param headers: словарь заголовков.
        :param auth: авторизация.
        :param cookies: cookies запроса.
        :param expected_codes: ожидаемые коды ответа.
        :return: Ответ.
        """
        headers = self._headers(headers=headers)
        expected_codes = self._expected_codes(expected_codes)
        response = _session.get(
            url=url, params=params, auth=auth, headers=headers, cookies=cookies
        )
        self.__log_request(response)
        built_in.should_contain(
            container=expected_codes,
            item=response.status_code,
            msg=f"Response status {response.status_code} not in allowed statuses {expected_codes}",
        )
        return response

    def _post(self, url: str, params=None, headers=None, json=None, data=None, auth=None, cookies=None,
              expected_codes=None) -> Response:
        """HTTP POST

        :param url: URL запроса.
        :param params: словарь параметров строки запроса.
        :param headers: словарь заголовков.
        :param json: тело запроса.
        :param data: данные запроса.
        :param auth: авторизация.
        :param cookies: cookies запроса.
        :param expected_codes: ожидаемые коды ответа.
        :return: Ответ.
        """
        headers = self._headers(headers=headers)
        expected_codes = self._expected_codes(expected_codes)
        response = _session.post(url=url, params=params, json=json, data=data, auth=auth, headers=headers,
                                 cookies=cookies)
        self.__log_request(response)
        built_in.should_contain(container=expected_codes, item=response.status_code,
                                msg=f"Response status {response.status_code} not in allowed statuses {expected_codes}")
        return response
