from .simple_exception_type import SimpleExceptionType


class SimpleException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str,
        err_type: SimpleExceptionType = SimpleExceptionType.NOT_SPECIFIED,
    ) -> None:
        super().__init__()
        self.status_code = status_code
        self.message = message
        self.err_type = err_type
