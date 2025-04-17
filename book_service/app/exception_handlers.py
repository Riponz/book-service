class BookBaseException(Exception):
    status_code = 500


class BookNotFoundException(BookBaseException):
    status_code = 404

    def __init__(self,message):
        super().__init__(message)

class NegetiveCountException(BookBaseException):
    status_code = 409

    def __init__(self,message):
        super().__init__(message)


class BookIntegrityException(BookBaseException):
    status_code = 400

    def __init__(self,message):
        super().__init__(message)

class BookOperationalException(BookBaseException):
    status_code = 500

    def __init__(self,message):
        super().__init__(message)

class BookDataException(BookBaseException):
    status_code = 422
    def __init__(self,message):
        super().__init__(message)

class BookTimeOutException(BookBaseException):
    status_code = 400

    def __init__(self,message):
        super().__init__(message)

