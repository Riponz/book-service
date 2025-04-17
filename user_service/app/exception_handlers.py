
class UserBaseException(Exception):
    status_code = 500

class DuplicateUserException(UserBaseException):
    status_code = 400

    def __init__(self,message):
        super().__init__(message)

class UserNotFoundException(UserBaseException):
    status_code = 404

    def __init__(self,message):
        super().__init__(message)


class UserIntegrityException(UserBaseException):
    status_code = 400

    def __init__(self,message):
        super().__init__(message)

class UserOperationalException(UserBaseException):
    status_code = 500

    def __init__(self,message):
        super().__init__(message)

class UserDataException(UserBaseException):
    status_code = 422
    def __init__(self,message):
        super().__init__(message)

class UserTimeOutException(UserBaseException):
    status_code = 400

    def __init__(self,message):
        super().__init__(message)

