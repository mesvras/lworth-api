class AppError(Exception):
    status_code = 500

    def __init__(self, message: str = "Erro interno"):
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):
    status_code = 404

    def __init__(self, entity: str, identifier: object):
        super().__init__(f"{entity} '{identifier}' não encontrado(a)")


class AlreadyExistsError(AppError):
    status_code = 409

    def __init__(self, entity: str, identifier: object):
        super().__init__(f"{entity} '{identifier}' já existe")


class UnauthorizedError(AppError):
    status_code = 401

    def __init__(self, message: str = "Não autenticadok"):
        super().__init__(message)


class ForbiddenError(AppError):
    status_code = 403

    def __init__(self, message: str = "Sem permissão"):
        super().__init__(message)
