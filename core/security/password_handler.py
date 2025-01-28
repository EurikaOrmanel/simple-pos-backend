from passlib.context import CryptContext


class PasswordHandler:
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str) -> str:
        return PasswordHandler.__pwd_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        return PasswordHandler.__pwd_context.verify(plain_password, hashed_password)
