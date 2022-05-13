from attr import has
import bcrypt

salt_times = 10


def encrypt_password(passw: str) -> str:
    passw = passw.encode('utf-8')
    hashed = bcrypt.hashpw(passw, bcrypt.gensalt(salt_times))
    return hashed


def compare_passwords(passw: str, hashed: str) -> bool:
    passw = passw.encode('utf-8')
    hashed = hashed.encode('utf-8')

    return True if bcrypt.checkpw(passw, hashed) else False
