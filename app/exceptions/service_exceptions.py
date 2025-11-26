from .base import AppException

class NotFoundError(AppException):
    pass

class ValidationError(AppException):
    pass

class LimitReachedError(AppException):
    pass
