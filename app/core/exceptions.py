import logging
from fastapi.requests import Request


logger = logging.getLogger(__name__)


class APIException(Exception):
    """
    This is API exception
    """

    def __init__(self, error_code: int = 000, status_code: int = 500, detail="", message="", *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

        self.error_code = error_code
        self.message = message
        self.detail = detail
        self.status_code = status_code

    def __str__(self):
        return f"APIException(status_code={self.status_code}, detail={self.message})"


async def log_request_info(request: Request):
    request_body = await request.json()

    logger.info(
        f"{request.method} request to {request.url} metadata\n"
        f"\tHeaders: {request.headers}\n"
        f"\tBody: {request_body}\n"
        f"\tPath Params: {request.path_params}\n"
        f"\tQuery Params: {request.query_params}\n"
        f"\tCookies: {request.cookies}\n"
    )
